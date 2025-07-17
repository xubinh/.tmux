#!/usr/bin/env python3

import os
import os.path
import re


def read_from_file(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf8") as file:
            content = file.read()
            return content
    except:
        raise


def write_to_file(file_path: str, content: str) -> None:
    try:
        with open(file_path, "w", encoding="utf8") as file:
            file.write(content)
    except:
        raise


def move_file_to_dir(file_path: str, target_dir: str) -> None:
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    assert os.path.isdir(target_dir)

    target_path = os.path.join(target_dir, os.path.basename(file_path))
    if os.path.exists(target_path):
        assert not os.path.isdir(target_path)
        os.rename(target_path, target_path + ".bak")

    os.rename(file_path, target_path)


def strip_triple_quote_string(content: str) -> str:
    assert content[0] == "\n"
    content = content[1:]
    content = re.sub(r"^ *", "", content, flags=re.MULTILINE)
    return content


def strip_shebang(content: str) -> str:
    content = re.sub(r"^#![^\n]*\n*", "", content)
    return content


def comment_entire_sh_script(content: str) -> str:
    assert content.strip()
    content_lines = content.split("\n")
    commented_lines = [("# " + line).strip() for line in content_lines]
    if commented_lines[-1] == "#":
        commented_lines[-1] = ""
    return "\n".join(commented_lines)


def get_tmux_conf_component_1() -> str:
    return ""


def get_tmux_conf_component_2() -> str:
    return "# : << 'EOF'\n"


def get_tmux_conf_component_3() -> str:
    content = """
        # Oh my tmux!
        # 💛🩷💙🖤❤️🤍
        # https://github.com/gpakosz/.tmux
        # (‑●‑●)> dual licensed under the WTFPL v2 license and the MIT license,
        #         without any warranty.
        #         Copyright 2012— Gregory Pakosz (@gpakosz).
        #
        # ------------------------------------------------------------------------------
        # 🚨 DO NOT MODIFY THIS FILE
        #      instead, override your .local customization file copy, see README.md
        # ------------------------------------------------------------------------------


    """
    return strip_triple_quote_string(content)


def get_tmux_conf_component_4() -> str:
    with open(".tmux.conf.part_tmux", "r", encoding="utf8") as file:
        content = file.read()
        return content


def get_tmux_conf_component_5() -> str:
    return "\n"


def get_tmux_conf_component_6() -> str:
    return "# EOF\n"


def get_tmux_conf_component_7() -> str:
    return "#\n"


def get_tmux_conf_component_8() -> str:
    with open(".tmux.conf.part_sh", "r", encoding="utf8") as file:
        content = file.read()

    content = strip_shebang(content)
    content = comment_entire_sh_script(content)
    return content


def get_tmux_conf_component_9() -> str:
    return ""


def build_tmux_conf() -> str:
    components = [
        get_tmux_conf_component_1(),
        get_tmux_conf_component_2(),
        get_tmux_conf_component_3(),
        get_tmux_conf_component_4(),
        get_tmux_conf_component_5(),
        get_tmux_conf_component_6(),
        get_tmux_conf_component_7(),
        get_tmux_conf_component_8(),
        get_tmux_conf_component_9(),
    ]
    return "".join(components)


def get_tmux_conf_local_component_1() -> str:
    return ""


def get_tmux_conf_local_component_2() -> str:
    return "# : << 'EOF'\n"


def get_tmux_conf_local_component_3() -> str:
    content = """
        # Oh my tmux!
        # 💛🩷💙🖤❤️🤍
        # https://github.com/gpakosz/.tmux
        # (‑●‑●)> dual licensed under the WTFPL v2 license and the MIT license,
        #         without any warranty.
        #         Copyright 2012— Gregory Pakosz (@gpakosz).


    """
    return strip_triple_quote_string(content)


def get_tmux_conf_local_component_4() -> str:
    with open(".tmux.conf.local.part_tmux", "r", encoding="utf8") as file:
        content = file.read()
        return content


def get_tmux_conf_local_component_5() -> str:
    content = r"""


        # -- custom variables ----------------------------------------------------------

        # to define a custom #{foo} variable, define a POSIX shell function between the
        # '# EOF' and the '# "$@"' lines. Please note that the opening brace { character
        # must be on the same line as the function name otherwise the parse won't detect
        # it.
        #
        # then, use #{foo} in e.g. the 'tmux_conf_theme_status_left' or the
        # 'tmux_conf_theme_status_right' variables.

        # ------------------------------------------------------------------------------

        # # /!\ do not remove the following line
    """
    return strip_triple_quote_string(content)


def get_tmux_conf_local_component_6() -> str:
    return "# EOF\n"


def get_tmux_conf_local_component_7() -> str:
    content = r"""
        #
        # # /!\ do not "uncomment" the functions: the leading "# " characters are needed
        #
    """
    return strip_triple_quote_string(content)


def get_tmux_conf_local_component_8() -> str:
    with open(".tmux.conf.local.part_sh", "r", encoding="utf8") as file:
        content = file.read()

    content = strip_shebang(content)
    content = comment_entire_sh_script(content)
    return content


def get_tmux_conf_local_component_9() -> str:
    content = r"""
        # # /!\ do not remove the previous line
        # #     do not write below this line
    """
    return strip_triple_quote_string(content)


def build_tmux_conf_local() -> str:
    components = [
        get_tmux_conf_local_component_1(),
        get_tmux_conf_local_component_2(),
        get_tmux_conf_local_component_3(),
        get_tmux_conf_local_component_4(),
        get_tmux_conf_local_component_5(),
        get_tmux_conf_local_component_6(),
        get_tmux_conf_local_component_7(),
        get_tmux_conf_local_component_8(),
        get_tmux_conf_local_component_9(),
    ]
    return "".join(components)


def main() -> None:
    # `.tmux.conf`
    content_of_tmux_conf = build_tmux_conf()
    write_to_file(".tmux.conf", content_of_tmux_conf)
    move_file_to_dir(".tmux.conf", "~/")

    # `.tmux.conf.local`
    content_of_tmux_conf_local = build_tmux_conf_local()
    write_to_file(".tmux.conf.local", content_of_tmux_conf_local)
    move_file_to_dir(".tmux.conf.local", "~/")


if __name__ == "__main__":
    main()
