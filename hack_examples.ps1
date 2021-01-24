$a = Get-ChildItem -Path 'src/cq_examples' -Filter 'Ex*.py' | Resolve-Path -Relative
foreach ($path in $a) {

    $module = $path.replace("./", "")
    $module = $module.replace("/", ".")
    $module = $module.replace(".py", "")
    
    $number = $path.replace("./src/cq_examples/Ex", "").SubString(0,3)

$script = 
@"
import unittest
import $module as ex

class TestExample$number(unittest.TestCase):
    def test_Ex$number(self):
        # Import and validate
        R = ex.result
        self.assertTrue(R.val().isValid())
"@

    $int_number = [int]$number
    if ( $int_number -gt 7 ) {
        echo $script > "./src/cq_examples/test_ex$number.py"
    }

}
