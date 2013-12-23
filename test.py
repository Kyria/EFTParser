import unittest
from eftparser import EFTParser


class EFTParsingTestCase(unittest.TestCase):

    def setUp(self):
        self.standard_fit = """
            [Naglfar, TestFit]
            
            Siege Module II
            6x2500mm Repeating Artillery I, Arch Angel EMP XL
            6x2500mm Repeating Artillery I, Arch Angel EMP XL
            
            Tracking Computer II, Tracking Speed Script
            Tracking Computer II, Tracking Speed Script
            Tracking Computer II, Optimal Range Script
            Sensor Booster II, Scan Resolution Script
            Sensor Booster II, Scan Resolution Script
            Republic Fleet Target Painter
            
            Capital Armor Repairer I
            Gyrostabilizer II
            Gyrostabilizer II
            Gyrostabilizer II
            Damage Control II
            Energized Adaptive Nano Membrane II
            
            Capital Projectile Ambit Extension II
            Capital Trimark Armor Pump I
            Capital Projectile Metastasis Adjuster I
        """
        
        self.fit_with_drones_and_ammunition = """
            [Dominix, TestFit With Cargo And Drone bay]
            Armor Explosive Hardener II
            Pseudoelectron Containment Field I
            1600mm Reinforced Steel Plates II
            Armor Kinetic Hardener II
            1600mm Reinforced Steel Plates II
            Energized Adaptive Nano Membrane II
            Armor Thermic Hardener II
            
            Prototype 100MN Microwarpdrive I
            Omnidirectional Tracking Link II
            Omnidirectional Tracking Link II
            Omnidirectional Tracking Link II
            Heavy Capacitor Booster II, Navy Cap Booster 800
            
            Heavy Unstable Power Fluctuator I
            Drone Link Augmentor II
            Drone Link Augmentor II
            Drone Link Augmentor II
            Drone Link Augmentor II
            Heavy Unstable Power Fluctuator I
            
            Large Trimark Armor Pump I
            Large Trimark Armor Pump I
            Large Trimark Armor Pump I
            
            Garde II x5
            Garde II x5
            Bouncer II x5
            Navy Cap Booster 800 x20
        """
        
        self.empty_fit = """ 
            [Sample NonRealShip To Test, Empty Fit]
            [Empty Subsystem slot]
            [Empty Subsystem slot]
            [Empty Subsystem slot]
            [Empty Subsystem slot]
            [Empty Subsystem slot]
            
            [Empty Low slot]
            [Empty Low slot]
            [Empty Low slot]
            [Empty Low slot]
            [Empty Low slot]
            
            [Empty Med slot]
            [Empty Med slot]
            [Empty Med slot]
            [Empty Med slot]
            [Empty Med slot]
            [Empty Med slot]
            
            [Empty High slot]
            [Empty High slot]
            [Empty High slot]
            [Empty High slot]
            [Empty High slot]
            [Empty High slot]
            [Empty High slot]
            [Empty High slot]
            
            [Empty Rig slot]
            [Empty Rig slot]
            [Empty Rig slot]

        """

        self.parser = ()
        
    def test_parsing_standard_fit(self):
        fit = EFTParser.parse(self.standard_fit)
        self.assertEqual(fit['ship_type']   ,'Naglfar')
        self.assertEqual(fit['fit_name']    ,'TestFit')
        
        self.assertEqual(len(fit['modules']) , 18)

        self.assertEqual(fit['modules'][0]['name']   ,'Siege Module II')
        self.assertEqual(fit['modules'][0]['charge'] ,'')        
        self.assertEqual(fit['modules'][1]['name']   ,'6x2500mm Repeating Artillery I')
        self.assertEqual(fit['modules'][1]['charge'] ,'Arch Angel EMP XL')      
        self.assertEqual(fit['modules'][2]['name']   ,'6x2500mm Repeating Artillery I')
        self.assertEqual(fit['modules'][2]['charge'] ,'Arch Angel EMP XL')
              
        self.assertEqual(fit['modules'][3]['name']   ,'Tracking Computer II')
        self.assertEqual(fit['modules'][3]['charge'] ,'Tracking Speed Script')      
        self.assertEqual(fit['modules'][4]['name']   ,'Tracking Computer II')
        self.assertEqual(fit['modules'][4]['charge'] ,'Tracking Speed Script')      
        self.assertEqual(fit['modules'][5]['name']   ,'Tracking Computer II')
        self.assertEqual(fit['modules'][5]['charge'] ,'Optimal Range Script')      
        self.assertEqual(fit['modules'][6]['name']   ,'Sensor Booster II')
        self.assertEqual(fit['modules'][6]['charge'] ,'Scan Resolution Script')      
        self.assertEqual(fit['modules'][7]['name']   ,'Sensor Booster II')
        self.assertEqual(fit['modules'][7]['charge'] ,'Scan Resolution Script')      
        self.assertEqual(fit['modules'][8]['name']   ,'Republic Fleet Target Painter')
        self.assertEqual(fit['modules'][8]['charge'] ,'') 
             
        self.assertEqual(fit['modules'][9]['name']   ,'Capital Armor Repairer I')
        self.assertEqual(fit['modules'][9]['charge'] ,'')      
        self.assertEqual(fit['modules'][10]['name']   ,'Gyrostabilizer II')
        self.assertEqual(fit['modules'][10]['charge'] ,'')      
        self.assertEqual(fit['modules'][11]['name']   ,'Gyrostabilizer II')
        self.assertEqual(fit['modules'][11]['charge'] ,'')      
        self.assertEqual(fit['modules'][12]['name']   ,'Gyrostabilizer II')
        self.assertEqual(fit['modules'][12]['charge'] ,'')      
        self.assertEqual(fit['modules'][13]['name']   ,'Damage Control II')
        self.assertEqual(fit['modules'][13]['charge'] ,'')      
        self.assertEqual(fit['modules'][14]['name']   ,'Energized Adaptive Nano Membrane II')
        self.assertEqual(fit['modules'][14]['charge'] ,'')
        
        self.assertEqual(fit['modules'][15]['name']   ,'Capital Projectile Ambit Extension II')
        self.assertEqual(fit['modules'][15]['charge'] ,'')      
        self.assertEqual(fit['modules'][16]['name']   ,'Capital Trimark Armor Pump I')
        self.assertEqual(fit['modules'][16]['charge'] ,'')      
        self.assertEqual(fit['modules'][17]['name']   ,'Capital Projectile Metastasis Adjuster I')
        self.assertEqual(fit['modules'][17]['charge'] ,'')


        self.assertEqual(len(fit['cargodrones']) , 0)


    def test_parsing_ammo_drone_fit(self):
        fit = EFTParser.parse(self.fit_with_drones_and_ammunition)
        self.assertEqual(fit['ship_type']   ,'Dominix')
        self.assertEqual(fit['fit_name']    ,'TestFit With Cargo And Drone bay')
    
        self.assertEqual(len(fit['modules']) , 21)
        
        self.assertEqual(fit['modules'][0]['name']    ,'Armor Explosive Hardener II')
        self.assertEqual(fit['modules'][0]['charge']  ,'')    
        self.assertEqual(fit['modules'][1]['name']    ,'Pseudoelectron Containment Field I')
        self.assertEqual(fit['modules'][1]['charge']  ,'')    
        self.assertEqual(fit['modules'][2]['name']    ,'1600mm Reinforced Steel Plates II')
        self.assertEqual(fit['modules'][2]['charge']  ,'')    
        self.assertEqual(fit['modules'][3]['name']    ,'Armor Kinetic Hardener II')
        self.assertEqual(fit['modules'][3]['charge']  ,'')    
        self.assertEqual(fit['modules'][4]['name']    ,'1600mm Reinforced Steel Plates II')
        self.assertEqual(fit['modules'][4]['charge']  ,'')    
        self.assertEqual(fit['modules'][5]['name']    ,'Energized Adaptive Nano Membrane II')
        self.assertEqual(fit['modules'][5]['charge']  ,'')    
        self.assertEqual(fit['modules'][6]['name']    ,'Armor Thermic Hardener II')
        self.assertEqual(fit['modules'][6]['charge']  ,'')
                                                      
        self.assertEqual(fit['modules'][7]['name']    ,'Prototype 100MN Microwarpdrive I')
        self.assertEqual(fit['modules'][7]['charge']  ,'')    
        self.assertEqual(fit['modules'][8]['name']    ,'Omnidirectional Tracking Link II')
        self.assertEqual(fit['modules'][8]['charge']  ,'')    
        self.assertEqual(fit['modules'][9]['name']    ,'Omnidirectional Tracking Link II')
        self.assertEqual(fit['modules'][9]['charge']  ,'')    
        self.assertEqual(fit['modules'][10]['name']   ,'Omnidirectional Tracking Link II')
        self.assertEqual(fit['modules'][10]['charge'] ,'')    
        self.assertEqual(fit['modules'][11]['name']   ,'Heavy Capacitor Booster II')
        self.assertEqual(fit['modules'][11]['charge'] ,'Navy Cap Booster 800')
                                                      
        self.assertEqual(fit['modules'][12]['name']   ,'Heavy Unstable Power Fluctuator I')
        self.assertEqual(fit['modules'][12]['charge'] ,'') 
        self.assertEqual(fit['modules'][13]['name']   ,'Drone Link Augmentor II')
        self.assertEqual(fit['modules'][13]['charge'] ,'') 
        self.assertEqual(fit['modules'][14]['name']   ,'Drone Link Augmentor II')
        self.assertEqual(fit['modules'][14]['charge'] ,'') 
        self.assertEqual(fit['modules'][15]['name']   ,'Drone Link Augmentor II')
        self.assertEqual(fit['modules'][15]['charge'] ,'') 
        self.assertEqual(fit['modules'][16]['name']   ,'Drone Link Augmentor II')
        self.assertEqual(fit['modules'][16]['charge'] ,'') 
        self.assertEqual(fit['modules'][17]['name']   ,'Heavy Unstable Power Fluctuator I')
        self.assertEqual(fit['modules'][17]['charge'] ,'') 
                                                      
        self.assertEqual(fit['modules'][18]['name']   ,'Large Trimark Armor Pump I')
        self.assertEqual(fit['modules'][18]['charge'] ,'') 
        self.assertEqual(fit['modules'][19]['name']   ,'Large Trimark Armor Pump I')
        self.assertEqual(fit['modules'][19]['charge'] ,'') 
        self.assertEqual(fit['modules'][20]['name']   ,'Large Trimark Armor Pump I')
        self.assertEqual(fit['modules'][20]['charge'] ,'')          

        self.assertEqual(len(fit['cargodrones']) , 4)     
        
        self.assertEqual(fit['cargodrones'][0]['name']     ,'Garde II')
        self.assertEqual(fit['cargodrones'][0]['quantity'] ,5) 
        self.assertEqual(fit['cargodrones'][1]['name']     ,'Garde II')
        self.assertEqual(fit['cargodrones'][1]['quantity'] ,5) 
        self.assertEqual(fit['cargodrones'][2]['name']     ,'Bouncer II')
        self.assertEqual(fit['cargodrones'][2]['quantity'] ,5) 
        self.assertEqual(fit['cargodrones'][3]['name']     ,'Navy Cap Booster 800')
        self.assertEqual(fit['cargodrones'][3]['quantity'] ,20)    
        
        
    def test_parsing_empty_fit(self):
        fit = EFTParser.parse(self.empty_fit)
        self.assertEqual(fit['ship_type']   ,'Sample NonRealShip To Test')
        self.assertEqual(fit['fit_name']    ,'Empty Fit')
        
        self.assertEqual(len(fit['modules']) , 0)
        self.assertEqual(len(fit['cargodrones']) , 0)
        
         
def suite():
    suite = unittest.TestSuite()
    suite.addTest(EFTParsingTestCase('test_parsing_standard_fit'))
    suite.addTest(EFTParsingTestCase('test_parsing_ammo_drone_fit'))
    suite.addTest(EFTParsingTestCase('test_parsing_empty_fit'))
    return suite
    
            
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=3).run(suite())
