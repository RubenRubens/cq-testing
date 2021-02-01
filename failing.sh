cd failing

lines=$(find * -name "test*.py" -exec echo {} \;)
exit_status=0
non_failing=""

for path in ${lines}
do
    echo $'\n\n'
    echo 💻 🧪 Test ${path} 🧪 💻
    timeout --foreground -k 60 60 python -m unittest ${path}
    if [[ ${?} -eq 0 ]]
    then
        exit_status=1
        non_failing+="${path}\n"
    fi
    echo $'\n\n'
done

# Display non passing tests
if [[ ${exit_status} -eq 1 ]]
then
    echo 'Non failing tests:'
    printf ${non_failing}
fi

# Exit with 1 if any test have not fail, exit with 0 otherwise
exit ${exit_status}
