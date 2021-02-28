#!/bin/bash
ssh manager << EOF
docker stack deploy --compose-file docker-compose.yaml project2
EOF
