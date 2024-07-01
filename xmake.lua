add_rules("mode.debug", "mode.release")

target("durango")
    set_kind("binary")
    add_files("components/**.cpp")
