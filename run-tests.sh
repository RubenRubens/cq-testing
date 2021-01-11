find * -name "test*.py" \
-exec echo $'\n\n\n💻 🧪 Test {} 🧪 💻' \; \
-exec timeout --foreground -k 20 20 \
python -m unittest {} \;