#!/bin/bash

set -e
set +x

source .env

show_help() {
    echo """
Usage: bash crystal.sh <command>
"""
}

case "$1" in
    run)
        docker-compose -f docker-compose.yml down; docker-compose -f docker-compose.yml up --build -d
    ;;
    run-debug)
        docker-compose -f docker-compose.yml down; docker-compose -f docker-compose.yml up --build
    ;;
    stop)
        docker-compose -f docker-compose.yml down
    ;;
    *)
        show_help
    ;;
esac
