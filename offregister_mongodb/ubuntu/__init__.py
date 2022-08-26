from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.ubuntu.systemd import restart_systemd
from patchwork.files import append


def install0(**kwargs):
    installed = lambda: c.run(
        "dpkg-query --showformat='${Version}' --show mongodb-org", hide=True
    )

    def mongodb_apt_init():
        if kwargs["VERSION"] == "3.4":
            c.sudo(
                "apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6"
            )
            c.sudo("rm /etc/apt/sources.list.d/mongodb-org*")
            append(
                "/etc/apt/sources.list.d/mongodb-org-3.4.list",
                "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse",
                use_sudo=True,
            )
        elif kwargs["VERSION"] == "3.6":
            c.sudo(
                "apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5"
            )
            c.sudo("rm /etc/apt/sources.list.d/mongodb-org*")
            append(
                "/etc/apt/sources.list.d/mongodb-org-3.6.list",
                "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse",
                use_sudo=True,
            )
        else:
            raise NotImplementedError(
                "MongoDB version {}; update the package, or use '3.4' | '3.6'".format(
                    kwargs["VERSION"]
                )
            )

    if c.sudo("dpkg -s mongodb-org", hide=True, warn=True).exited != 0:
        mongodb_apt_init()
        apt_depends(c, "mongodb-org")
        restart_systemd("mongod")
        return "MongoDB {} installed".format(installed())

    version = installed()
    if not version.startswith(kwargs["VERSION"]):
        mongodb_apt_init()
        apt_depends(c, "mongodb-org")
        restart_systemd("mongod")
        return "MongoDB {} installed".format(installed())

    return "[Already] MongoDB {} installed".format(installed())
