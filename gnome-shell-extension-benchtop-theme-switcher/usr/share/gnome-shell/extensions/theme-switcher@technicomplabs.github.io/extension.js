/* extension.js
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * SPDX-License-Identifier: GPL-2.0-or-later
 *
 * Benchtop Theme Switcher, the Technicomp Benchtop Linux fork of Legacy (GTK3)
 * Theme Scheme Auto Switcher by Mukul Joshi
 * (https://github.com/mukul29/legacy-theme-auto-switcher-gnome-extension).
 * TCBL changes: the Kvantum theme of Qt applications is switched as well.
 */

/* exported Extension */
import Gio from 'gi://Gio';
import GLib from 'gi://GLib';

const DEFAULT_SCHEME_NAME = 'default';
const LIGHT_SCHEME_NAME = 'prefer-light';
const DARK_SCHEME_NAME = 'prefer-dark';

// TCBL: Kvantum, the Qt style. Its chosen theme is in
// ~/.config/Kvantum/kvantum.kvconfig; themes are in ~/.config/Kvantum and
// /usr/share/Kvantum. A theme's dark variant, NameDark, is kept in the folder
// of the light theme, Name, as Kvantum itself looks for it.
const KVANTUM_CONFIG_DIR = GLib.build_filenamev([GLib.get_user_config_dir(), 'Kvantum']);
const KVANTUM_CONFIG = GLib.build_filenamev([KVANTUM_CONFIG_DIR, 'kvantum.kvconfig']);
const KVANTUM_THEME_DIRS = [KVANTUM_CONFIG_DIR, '/usr/share/Kvantum'];

function kvantumThemeExists(name) {
    const folders = [name];
    if (name.endsWith('Dark'))
        folders.push(name.slice(0, -4));
    return KVANTUM_THEME_DIRS.some(dir => folders.some(folder =>
        GLib.file_test(GLib.build_filenamev([dir, folder, `${name}.kvconfig`]), GLib.FileTest.EXISTS)));
}

// Switches the Kvantum theme to its dark variant (NameDark, also from
// NameLight) or back to its light one (Name), when that variant exists.
// Without a Kvantum configuration there is nothing to switch. Qt applications
// read the theme when they start.
function switchKvantumTheme(dark) {
    const config = new GLib.KeyFile();
    let theme;
    try {
        config.load_from_file(KVANTUM_CONFIG, GLib.KeyFileFlags.KEEP_COMMENTS);
        theme = config.get_string('General', 'theme');
    } catch (e) {
        return;
    }

    let target = null;
    if (dark && !theme.endsWith('Dark'))
        target = `${theme.endsWith('Light') ? theme.slice(0, -5) : theme}Dark`;
    else if (!dark && theme.endsWith('Dark'))
        target = theme.slice(0, -4);

    if (!target || !kvantumThemeExists(target))
        return;

    config.set_string('General', 'theme', target);
    try {
        config.save_to_file(KVANTUM_CONFIG);
    } catch (e) {
        logError(e, 'Benchtop Theme Switcher: cannot write the Kvantum configuration');
    }
}

export default class BenchtopThemeSwitcher {
    handleThemeChange = (theme_name) => {
        switch(theme_name)
        {
            case DEFAULT_SCHEME_NAME:
            case LIGHT_SCHEME_NAME:
                if (this.schema.get_string('gtk-theme').endsWith("-dark")) {
                    this.schema.set_string('gtk-theme', this.schema.get_string('gtk-theme').slice(0,-5));
                }
                switchKvantumTheme(false);    // TCBL
                break;
            case DARK_SCHEME_NAME:
                if (!this.schema.get_string('gtk-theme').endsWith("-dark")) {
                    this.schema.set_string('gtk-theme', this.schema.get_string('gtk-theme') + "-dark");
                }
                switchKvantumTheme(true);     // TCBL
                break;
            default:
                break;
        }
    }

    handleCurrentTheme = () => {
        let value = this.schema.get_string('color-scheme');
        this.handleThemeChange(value);
    }

    enable() {
        this.schema = Gio.Settings.new('org.gnome.desktop.interface');
        this.id = this.schema.connect('changed::color-scheme', () => {
            this.handleCurrentTheme();
        });
        this.handleCurrentTheme();
    }

    disable() {
        if (this.schema) {
            if (this.id) {
                this.schema.disconnect(this.id);
                this.id = null;
            }
            this.schema = null;
        }
    }
}
