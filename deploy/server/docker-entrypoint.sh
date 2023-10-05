#!/bin/bash

set -e
set +x

show_help() {
    echo """
Usage: docker run <imagename> COMMAND
"""
}

run_uwsgi_server() {
    python crystal/manage.py migrate
    collect_static
	uwsgi /opt/crystal/deploy/server/app.ini
}

collect_static() {
    python crystal/manage.py collectstatic --noinput -c
}

# Run
case "$1" in
    uwsgi)
        run_uwsgi_server
    ;;
    python)
        python "${@:2}"
    ;;
    bash)
        /bin/bash "${@:2}"
    ;;
    shell)
        python crystal/manage.py shell_plus
    ;;
    manage)
        python crystal/manage.py "${@:2}"
    ;;
    collect_static)
        collect_static
    ;;
    *)
        show_help
    ;;
esac
