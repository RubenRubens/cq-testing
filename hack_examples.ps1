$a = Get-ChildItem -Path 'src/cq_examples' -Filter 'Ex*.py' | Resolve-Path -Relative
$a | ForEach-Object {

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

    $module = $_.replace("./", "")
    $module = $module.replace("/", ".")
    $module = $module.replace(".py", "")
    
    $number = $_.replace("./src/cq_examples/Ex", "").SubString(0,3)
    
	if ( $number -as [int] -gt 7 ) {
    	echo $script > ./src/cq_examples/test_ex$number.py
	}

}
