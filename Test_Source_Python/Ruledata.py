CodingRule_CSharp = {
    "Dict": ['Adc', 'ADC','X2x','E2x', 'U2x','E2M', 'U2A16', 'U2A8', 'E2H', 'SGm', 'Renesas', 'SGm', 'Det', 'Dem', 'config', 'Ecm', 'Hw', 'ADTRGn', 'UI','LucChannel',
'LucScanGrp', 'Runtime', 'Cbk', 'Cfg', 'PbCfg', 'Gaa', 'Dma', 'Trigg', 'FCC1', 'E2UH', 'Item' ,'Param', 'Sg', 'Struct', 'Util', 'FCC2',
'foreach', 'hw', 'Clk', 'mcu', 'BswM', 'Api', 'sgDma', 'confured', 'Notif', 'Grp', 'struct', 'Sys', 'Cpu', 'Mcu','Sgs', 'adc','coverity',
'lookups', 'ResX', 'Src', 'TH', 'initializer', 'param', 'structs', 'Trg', 'DbToc', 'ul', 'ulStartOfDbToc', 'pSgUnitConfig', 'pGroupConfig',
'pGroupHWTrigg', 'pGroupSGTrigg', 'pTriggOutConfigValue', 'pTriggOutConfigRegister', 'pLimitCheckRange', 'pDmaUnitConfig', 'pDmaHWUnitMapping','params',
'pDmaSGUnitMapping', 'pChannelToGroup', 'pHwUnitIndex', 'pSgUnitIndex', 'p', 'Params', 'pre', 'pGroupRamData', 'pSgUnitRamData', 'pChannelToDisableEnable',
'ucMaxSwTriggGroups', 'ucNoOfGroups', 'ucMaxDmaChannels', 'ucNoOfChannels', 'pWaittimeConfig', 'dma', 'Index',
'pDma','uC','diag','VirChPtr','pGroup','ADCJTSEL','VC','pEic','pHw','pError','SG','pPic','numberic','Sg','pQueue',
'pTrigg','pSg','TSEL','PICADTENx','numberic','sw','Dem','DTC','FiM','Dev','DemB','Dtc','OBD','Nv','Dlt','Asynch','Isr','Pre','Conv',
'Voltsrc','Samp','Ckt','Num','Setm','us','SGVCOWR','VCULLMTBR','dd','sumchn','trigg','JnSFTCR','Misra','QacMapping','Gtm','Trigg',
'mimimum','demPara','demCon','configur','Commpute','cdf','XnVCRJ','overriden','ig','pDI','pVC','WAITTRy','VCULLMTBR','Commpute',
'PICADTENx','configurated','XnVCRJ','Gaa','Imr','pErr','Eic','Reg', 'Regs',
'chnLowLt','VCULLMTBR','ul','Vcr','vcr','lsb','Pic','pQueue','Sg','pSg','TSEL','uc','ulVcr','ulPICADTENx','Chk','Configs',
'sumchn','GTM','ara','Ref','Lsb','madatory','JnTRG','Lsb','intermendiateValue','Lsb','Diag', 'Pwm','Init','Registers',
'Dcm','ucVCRegIndex','VirCh','Ok','Prescale','SGVCOWRx'
    ],

    "File_Name": {

        1: {
            "Rule": "",
            "Status": "fully",
            "message": "File name shall use Pascal case and only consist of alphanumeric characters. But it shall not start with numeric."
        },
        2: {
            "Rule": 64,
            "Status": "fully",
            "message": "File name shall not contain more than 64 characters."
        },
        3: {
            "Rule": "",
            "Status": "fully",
            "message": "In case of MCU Driver related Generation Tool, the naming of the main file which contains program entry point shall be in following format: '<Msn>.cs'"
        },
        4: {
            "Rule": "",
            "Status": "fully",
            "message": "Source file for interface class should have prefix \"I\" \nEg: I<Component><Sub Component>.cs"
        },

        5: {
            "Rule": "",
            "Status": "fully",
            "message": "Do not use abbreviation, contraction or acronyms as part of file names if it is not widely accepted."
        }
    },

    "Variable_Name": {

        1: {
            "Rule": "",
            "Status": "fully",
            "message": "Use Camel case for local variables."
        },
        2: {
            "Rule": '',
            "Status": "fully",
            "message": "Use Pascal case for global variables."
        },
        3: {
            "Rule": "",
            "Status": "fully",
            "message": "A meaning full name (with respect to that context) should be given to the variables. Avoid giving name as Temp, Busy, etc."
        },
        4: {
            "Rule": "",
            "Status": "fully",
            "message": "Source file for interface class should have prefix \"I\" \nEg: I<Component><Sub Component>.cs"
        },

        5: {
            "Rule": "",
            "Status": "fully",
            "message": "The following rules should be applied for all variables naming:\n- Do not use Hungarian notation (to indicate the type of variable).\n- Do not use underscores."
        }
    },
    
    "Method_Name":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": "- Using Pascal case for public/protected methods and Camel case for private methods.\n- DO give methods names that are verbs or verb phrases.\n- DO NOT use the underscore character (_)."
        }
    },

     "Type_Name":{
        3: {
            "Rule": "",
            "Status": "fully",
            "message": """Names of enumeration types (also called enums) in general should follow below rules:
-	Using Pascal case for naming enumerations type.
-	Using a singular type name for an enumeration unless its values are bit fields.
-	Using a plural type name for an enumeration for masking bit fields or doing bitwise comparisons, also called flags enum.
-	DO NOT use an "Enum" suffix in enum type names.
-	DO NOT use "Flag" or "Flags" suffixes in enum type names.
-	DO NOT use a prefix on enumeration value names.
"""
        }
    },

    "Param_Name":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": """- DO use Camel case in parameter names.\n- DO use meaning full parameter names.\n- CONSIDER using names based on a parameter's meaning rather than the parameter's type.
"""
    },
},

    "Class_Name":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": """The following rules outline the guidelines for naming classes:
-	Use a noun or noun phrase to name a class.
-	Use Pascal case.
-	Use abbreviations sparingly.
-	Do not use a type prefix on a class name.
-	Do not use the underscore character (_).
-	Where appropriate, use a compound word to name a derived class. The second part of the derived class's name should be the name of the base class.
"""
    },
},
    "Event_Name":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": """Events naming should be followed below rules:
-	DO name event handlers (delegates used as types of events) with the "EventHandler" suffix.
-	DO use two parameters named sender and e in event handlers.
-	DO name event argument classes with the "EventArgs" suffix.
"""
    },
},
    "Field_Name":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": """Field naming should be followed below rules:
-	DO use Pascal case in public and protected field names.
-	DO use Camel case in private field names.
-	DO name fields using a noun, noun phrase, or adjective.
-	DO NOT use a prefix for field names.
"""
    },
},
    "Format":{
        5: {
            "Rule": "",
            "Status": "fully",
            "message": """Each line in source files shall be limited to 120 columns. If the statement exceeds 120 characters, use a 'carriage return' and indent 4 spaces to continue the statement on the next line."""
    },
        7: {
            "Rule": "",
            "Status": "fully",
            "message": """A space shall be used between 'if', 'else if', 'while', 'for', 'switch' and the opening parenthesis."""
    },
        8: {
        "Rule": "",
        "Status": "fully",
        "message": """Spaces shall not be used between unary operators and operands. Unary operators: '++', '--', '~', '!'. """
    },
        9: {
        "Rule": "",
        "Status": "fully",
        "message": """A space shall be used before and after a binary operator."""
    },
        10: {
        "Rule": "",
        "Status": "fully",
        "message": """A space shall be used after each comma in the argument or initialization list."""
    },
        11: {
        "Rule": "",
        "Status": "fully",
        "message": """Each expression statement shall be on a separate line."""
    },
        13: {
        "Rule": "",
        "Status": "fully",
        "message": """'#if' statements ('#if' - '#else' - '#endif') should be indented according to their nesting depth."""
    },
        14: {
        "Rule": "",
        "Status": "fully",
        "message": """Tabs and unwanted spaces shall not be present at the end of the line in make files."""
    },
        15: {
        "Rule": "",
        "Status": "fully",
        "message": """The constants shall be place on the left of equality comparisons."""
    },
        16: {
        "Rule": "",
        "Status": "fully",
        "message": """Check that all condition checks have variables of same type on RHS (right hand side) and LHS (left hand side) or there is explicit type casting."""
    },
},
    "File_Structure":{
        3: {
            "Rule": "",
            "Status": "fully",
            "message": """The source file should end with a blank line."""
    },
},
    "Comment":{
        4: {
            "Rule": "",
            "Status": "fully",
            "message": """The following C Sharp constructs shall be commented after the concluding bracket if they are longer than 10 lines:
'switch-case'
'if-then-else'
'do-while'
'for'"""
    },
        6: {
            "Rule": "",
            "Status": "fully",
            "message": """Comments shall not be nested."""
},

},
    "External":{
        3: {
            "Rule": "",
            "Status": "fully",
            "message": """In general, use int rather than unsigned types."""
    },
},
    "Rule_Comment":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": """All comments shall be in English and spell checked."""
    },
},
    "Types":{
        2: {
            "Rule": "",
            "Status": "fully",
            "message": """Integer values of the enumeration elements must not be used in calculations."""
    },
        4: {
        "Rule": "",
        "Status": "fully",
        "message": """Variables for loop counters must be declared in the generic type (e.g. 'int')."""
    },
},
    "Constant":{
        1: {
            "Rule": "",
            "Status": "fully",
            "message": """Hexadecimal constants shall be represented using all uppercase letters following 0x."""
    },
        4: {
            "Rule": "",
            "Status": "fully",
            "message": """Use all uppercase when naming constant. An underscore can be used to separate terms when necessary. """
    },
},
    "Declaration":{
        4: {
            "Rule": "",
            "Status": "fully",
            "message": """Multiple variable declarations shall not be allowed on the same line."""
    },
        12: {
            "Rule": "",
            "Status": "fully",
            "message": """Variables used in the code need to be defined; moreover, unused variables should not be contained."""
    },
        13: {
        "Rule": "",
        "Status": "fully",
        "message": """Unused input parameter(s) of function shall not be declared."""
    },
        27: {
        "Rule": "",
        "Status": "fully",
        "message": """Put declarations only at the beginning of blocks. (A block is any code surrounded by curly braces "{" and "}".) 
    Don't wait to declare variables until their first use."""
    },
},
}