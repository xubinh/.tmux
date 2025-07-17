#!/usr/bin/env python3


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


def get_tmux_conf_component_1() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_2() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_3() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_4() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_5() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_6() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_7() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_8() -> str:
    raise NotImplementedError()


def get_tmux_conf_component_9() -> str:
    raise NotImplementedError()


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
    raise NotImplementedError()


def get_tmux_conf_local_component_2() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_3() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_4() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_5() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_6() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_7() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_8() -> str:
    raise NotImplementedError()


def get_tmux_conf_local_component_9() -> str:
    raise NotImplementedError()


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
    write_to_file(".tmux.conf.tmp", content_of_tmux_conf)

    # `.tmux.conf.local`
    content_of_tmux_conf_local = build_tmux_conf()
    write_to_file(".tmux.conf.local.tmp", content_of_tmux_conf_local)


if __name__ == "__main__":
    main()
