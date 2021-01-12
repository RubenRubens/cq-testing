find * -name "test*.py" \
-exec echo $'\n\n\n💻 🧪 Test {} 🧪 💻' \; \
-exec timeout --foreground -k 60 60 \
python -m unittest {} \;