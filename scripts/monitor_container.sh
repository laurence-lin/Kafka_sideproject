#!/bin/bash

docker stats $(docker ps --filter  "ancestor=wurstmeister/kafka" --format {{.ID}})