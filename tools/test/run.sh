#!/usr/bin/env bash
# Starts the stub API server on :8791 serving public/, runs the checks, stops the server.
# Usage: bash tools/test/run.sh            (smoke + reviews render + member screener)
set -u
cd "$(dirname "$0")"
node server.mjs > server.log 2>&1 & PID=$!
sleep 1.5
STATUS=0
node smoke.cjs || STATUS=1
node rev.cjs || STATUS=1
node scr.cjs || STATUS=1
node traffic.cjs || STATUS=1
node panel.cjs || STATUS=1
kill $PID 2>/dev/null
exit $STATUS
