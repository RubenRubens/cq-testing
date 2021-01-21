lines=`cat passing.txt`
exit_status=0
failing=""

for path in ${lines}
do
    echo $'\n\n'
    echo 💻 🧪 Test ${path} 🧪 💻
    timeout --foreground -k 60 60 python -m unittest ${path}
    if [[ ${?} -ne 0 ]]
    then
        exit_status=1
        failing+="${path}\n"
    fi
    echo $'\n\n'
done

# Display non passing tests
if [[ ${exit_status} -eq 1 ]]
then
    echo 'Non passing tests:'
    printf ${failing}
fi

# Exit with 1 if any test failed, exit with 0 otherwise
exit ${exit_status}
