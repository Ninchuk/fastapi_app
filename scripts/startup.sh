#!/usr/bin/env bash

for argument in "$@"; do
  case $argument in

    -m | --migrate)
      printf "Alembic migration process...\n\n"
      alembic -c conf/alembic.ini upgrade head
      ;;

    *)
      echo "Unknown argument"
    ;;
  esac
done

echo "Start web application"
gunicorn -c conf/gunicorn.conf.py --timeout 180