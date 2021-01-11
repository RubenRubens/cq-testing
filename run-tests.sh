find * -name "test*.py" \
-exec echo $'\n\n\n💻 🧪 Test {} 🧪 💻' \; \
-exec timeout --foreground -k 10 10 \
python -m unittest {} \;