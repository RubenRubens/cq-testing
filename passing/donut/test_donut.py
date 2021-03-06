import unittest

class TestDonut(unittest.TestCase):
    
    def test_donut(self):
        import donut.donut
        global homer
        homer = donut.donut.result
        self.assertTrue(homer.val().isValid())

    def test_volume(self):
        from math import pi
        (R, r) = (30, 10)
        # volume of a torus
        vol = 2 * pi**2 * R * r**2
        self.assertAlmostEqual(homer.val().Volume(), vol)


#                        @@@@@@@@                                    
#                    ####$$$$$$$$@@@$$                               
#                  *******#####$$$$$$$$$$                            
#                 =====!!!!***#####$$$$$$$#                          
#                :;;;;;;==!!!****########$###                        
#                ::~~::;;;=!!=!!*****#########                       
#                --,,-~~~:;;;===!******#*#####**                     
#                ,.....,-~~:;:====!!*!***********                    
#                .........--~::;;===!!!*!********!                   
#                ..........,--~:;;;;==!!!!!*****!!                   
#                 ...........,-~~::;;===!=!!!!!!!!=                  
#                  ......,,-..,,-~::;;;====!=!!!!!=                  
#                  .,-~~~;;##..,,-~~::;;;==========;                 
#                   .-~;=*#$$@...,-~~:::;;;;;======;                 
#                     -;!!*#$$#...,--~~:::;;;;;;;;;:                 
#                      -;=!**!=~...,---~:::::;;;;;:                  
#                       ,:=:;;:-...,,,--~~~:::::::~                  
#                         -:;:~-.....,,--~~~~~~~~~                   
#                           ,--,.....,,,---------                    
#                             .........,,,,,,,,,                     
#                                .............     
