npm --prefix /app/src/server/frontend run dev -- --host &
echo $1
python3.8 src/server/run.py --host=0.0.0.0 $1