from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-name', )

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-name', )

    def __str__(self):
        return self.name


class Book(models.Model):

    class Languages(models.TextChoices):
        ENGLISH = 'en', 'English'
        RUSSIAN = 'ru', 'Russian'
        FRENCH = 'fr', 'French',
        SPANISH = 'es', 'Spanish',
        GERMAN = 'de', 'German',
        ITALIAN = 'it', 'Italian'

    class Topics(models.TextChoices):
        BUSINESS = 'BUSINESS', 'Business'
        BUSINESS_ACCOUNTING = 'BUSINESS:ACCOUNTING', 'Business:Accounting'
        BUSINESS_LOGISTICS = 'BUSINESS:LOGISTICS', 'Business:Logistics'
        BUSINESS_MARKETING = 'BUSINESS:MARKETING', 'Business:Marketing'
        BUSINESS_MARKETING_ADVERTISING = 'BUSINESS:MARKETING:ADVERTISING', 'Business:Marketing:Advertising'
        BUSINESS_MANAGEMENT = 'BUSINESS:MANAGEMENT', 'Business:Management'
        BUSINESS_MANAGEMENT_PROJECT_MANAGEMENT = 'BUSINESS:MANAGEMENT:PROJECT_MANAGEMENT', \
                                                 'Business:Management:Project_Management'
        BUSINESS_MLM = 'BUSINESS:MLM', 'Business:MLM'
        BUSINESS_RESPONSIBILITY_AND_BUSINESS_ETHICS = 'BUSINESS:RESPONSIBILITY_AND_BUSINESS_ETHICS', \
                                                      'Business:Responsibility_and_Business_Ethics'
        BUSINESS_TRADING = 'BUSINESS:TRADING', 'Business:Trading'
        BUSINESS_E_COMMERCE = 'BUSINESS:E-COMMERCE', 'Business:E-Commerce'
        BIOLOGY = 'BIOLOGY', 'Biology'
        BIOLOGY_ESTESTVOZNANANIE = 'BIOLOGY:ESTESTVOZNANANIE', 'Biology:Estestvoznananie'
        BIOLOGY_ANTHROPOLOGY = 'BIOLOGY:ANTHROPOLOGY', 'Biology:Anthropology'
        BIOLOGY_ANTHROPOLOGY_EVOLUTION = 'BIOLOGY:ANTHROPOLOGY:EVOLUTION', 'Biology:Anthropology:Evolution'
        BIOLOGY_BIOSTATISTICS = 'BIOLOGY:BIOSTATISTICS', 'Biology:Biostatistics'
        BIOLOGY_BIOTECHNOLOGY = 'BIOLOGY:BIOTECHNOLOGY', 'Biology:Biotechnology'
        BIOLOGY_BIOPHYSICS = 'BIOLOGY:BIOPHYSICS', 'Biology:Biophysics'
        BIOLOGY_BIOCHEMISTRY = 'BIOLOGY:BIOCHEMISTRY', 'Biology:Biochemistry'
        BIOLOGY_BIOCHEMISTRY_ENOLOGIST = 'BIOLOGY:BIOCHEMISTRY:ENOLOGIST', 'Biology:Biochemistry:enologist'
        BIOLOGY_VIROLOGY = 'BIOLOGY:VIROLOGY', 'Biology:Virology'
        BIOLOGY_GENETICS = 'BIOLOGY:GENETICS', 'Biology:Genetics'
        BIOLOGY_ZOOLOGY = 'BIOLOGY:ZOOLOGY', 'Biology:Zoology'
        BIOLOGY_ZOOLOGY_PALEONTOLOGY = 'BIOLOGY:ZOOLOGY:PALEONTOLOGY', 'Biology:Zoology:Paleontology'
        BIOLOGY_ZOOLOGY_FISH = 'BIOLOGY:ZOOLOGY:FISH', 'Biology:Zoology:Fish'
        BIOLOGY_MICROBIOLOGY = 'BIOLOGY:MICROBIOLOGY', 'Biology:Microbiology'
        BIOLOGY_MOLECULAR = 'BIOLOGY:MOLECULAR', 'Biology:Molecular'
        BIOLOGY_MOLECULAR_BIOINFORMATICS = 'BIOLOGY:MOLECULAR:BIOINFORMATICS', 'Biology:Molecular:Bioinformatics'
        BIOLOGY_PLANTS_BOTANY = 'BIOLOGY:PLANTS:BOTANY', 'Biology:Plants:Botany'
        BIOLOGY_PLANTS_AGRICULTURE_AND_FORESTRY = 'BIOLOGY:PLANTS:AGRICULTURE_AND_FORESTRY', \
                                                  'Biology:Plants:Agriculture_and_Forestry'
        BIOLOGY_ECOLOGY = 'BIOLOGY:ECOLOGY', 'Biology:Ecology'
        GEOGRAPHY = 'GEOGRAPHY', 'Geography'
        GEOGRAPHY_GEODESY_CARTOGRAPHY = 'GEOGRAPHY:GEODESY._CARTOGRAPHY', 'Geography:Geodesy._Cartography'
        GEOGRAPHY_LOCAL_HISTORY = 'GEOGRAPHY:LOCAL_HISTORY', 'Geography:Local_History'
        GEOGRAPHY_LOCAL_HISTORY_TOURISM = 'GEOGRAPHY:LOCAL_HISTORY:TOURISM', 'Geography:Local_history:Tourism'
        GEOGRAPHY_METEOROLOGY, _CLIMATOLOGY = 'GEOGRAPHY:METEOROLOGY,_CLIMATOLOGY', 'Geography:Meteorology,_Climatology'
        GEOGRAPHY_RUSSIA = 'GEOGRAPHY:RUSSIA', 'Geography:Russia'
        GEOLOGY = 'GEOLOGY', 'Geology'
        GEOLOGY_HYDROGEOLOGY = 'GEOLOGY:HYDROGEOLOGY', 'Geology:Hydrogeology'
        GEOLOGY_MINING = 'GEOLOGY:MINING', 'Geology:Mining'
        HOUSEKEEPING_LEISURE = 'HOUSEKEEPING_LEISURE', 'Housekeeping_leisure'
        HOUSEKEEPING_LEISURE_AQUARIA = 'HOUSEKEEPING_LEISURE:AQUARIA', 'Housekeeping_leisure:Aquaria'
        HOUSEKEEPING_LEISURE_ASTROLOGY = 'HOUSEKEEPING_LEISURE:ASTROLOGY', 'Housekeeping_leisure:Astrology'
        HOUSEKEEPING_LEISURE_PET = 'HOUSEKEEPING_LEISURE:PET', 'Housekeeping_leisure:Pet'
        HOUSEKEEPING_LEISURE_GAMES_BOARD_GAMES = 'HOUSEKEEPING_LEISURE:GAMES:BOARD_GAMES', \
                                                 'Housekeeping_leisure:Games:Board_Games'
        HOUSEKEEPING_LEISURE_GAMES_CHESS = 'HOUSEKEEPING_LEISURE:GAMES:CHESS', 'Housekeeping_leisure:Games:Chess'
        HOUSEKEEPING_LEISURE_COLLECTING = 'HOUSEKEEPING_LEISURE:COLLECTING', 'Housekeeping,_leisure:Collecting'
        HOUSEKEEPING_LEISURE_BEAUTY, _IMAGE = 'HOUSEKEEPING_LEISURE:BEAUTY,_IMAGE', 'Housekeeping,_leisure:Beauty_image'
        HOUSEKEEPING_LEISURE_COOKING = 'HOUSEKEEPING_LEISURE:COOKING', 'Housekeeping,_leisure:Cooking'
        HOUSEKEEPING_LEISURE_FASHION, _JEWELRY = 'HOUSEKEEPING_LEISURE:FASHION_JEWELRY', \
                                                 'Housekeeping,_leisure:Fashion_Jewelry'
        HOUSEKEEPING_LEISURE_HUNTING_AND_GAME_MANAGEMENT = 'HOUSEKEEPING_LEISURE:HUNTING_AND_GAME_MANAGEMENT', \
                                                           'Housekeeping_leisure:Hunting_and_Game_Management'
        HOUSEKEEPING_LEISURE_BENEFITS_HOMEBREW = 'HOUSEKEEPING_LEISURE:BENEFITS_HOMEBREW', \
                                                 'Housekeeping_leisure:Benefits_Homebrew'
        HOUSEKEEPING_LEISURE_PROFESSIONS_AND_TRADES = 'HOUSEKEEPING_LEISURE:PROFESSIONS_AND_TRADES', \
                                                      'Housekeeping_leisure:Professions_and_Trades'
        HOUSEKEEPING_LEISURE_HANDICRAFT = 'HOUSEKEEPING_LEISURE:HANDICRAFT', 'Housekeeping_leisure:Handicraft'
        HOUSEKEEPING_LEISURE_HANDICRAFT_CUTTING_AND_SEWING = 'HOUSEKEEPING_LEISURE:HANDICRAFT:CUTTING_AND_SEWING', \
                                                             'Housekeeping_leisure:Handicraft:Cutting_and_Sewing'
        HOUSEKEEPING_LEISURE_GARDEN, _GARDEN = 'HOUSEKEEPING_LEISURE:GARDEN,_GARDEN', \
                                               'Housekeeping_leisure:Garden,_garden'
        ART = 'ART', 'Art'
        ART_DESIGN_ARCHITECTURE = 'ART:DESIGN:ARCHITECTURE', 'Art:Design:Architecture'
        ART_GRAPHIC_ARTS = 'ART:GRAPHIC_ARTS', 'Art:Graphic_Arts'
        ART_CINEMA = 'ART:CINEMA', 'Art:Cinema'
        ART_MUSIC = 'ART:MUSIC', 'Art:Music'
        ART_MUSIC_GUITAR = 'ART:MUSIC:GUITAR', 'Art:Music:Guitar'
        ART_PHOTO = 'ART:PHOTO', 'Art:Photo'
        HISTORY = 'HISTORY', 'History'
        HISTORY_AMERICAN_STUDIES = 'HISTORY:AMERICAN_STUDIES', 'History:American_Studies'
        HISTORY_ARCHAEOLOGY = 'HISTORY:ARCHAEOLOGY', 'History:Archaeology'
        HISTORY_MILITARY_HISTORY = 'HISTORY:MILITARY_HISTORY', 'History:Military_History'
        HISTORY_MEMOIRS, _BIOGRAPHIES = 'HISTORY:MEMOIRS,_BIOGRAPHIES', 'History:Memoirs,_Biographies'
        COMPUTERS = 'COMPUTERS', 'Computers'
        COMPUTERS_WEB_DESIGN = 'COMPUTERS:WEB_DESIGN', 'Computers:Web_design'
        COMPUTERS_ALGORITHMS_AND_DATA_STRUCTURES = 'COMPUTERS:ALGORITHMS_AND_DATA_STRUCTURES', \
                                                   'Computers:Algorithms_and_Data_Structures'
        COMPUTERS_ALGORITHMS_AND_DATA_STRUCTURES_CRYPTOGRAPHY = 'COMPUTERS:ALGORITHMS_AND_DATA_STRUCTURES:CRYPTOGRAPHY',\
                                                                'Computers:Algorithms_and_Data_Structures:Cryptography'
        COMPUTERS_ALGORITHMS_AND_DATA_STRUCTURES_IMAGE_PROCESSING = 'COMPUTERS:ALGORITHMS_AND_DATA_STRUCTURES:IMAGE_PROCESSING', \
                                                                    'Computers:Algorithms_and_Data_Structures:Image_Processing'
        COMPUTERS_ALGORITHMS_AND_DATA_STRUCTURES_PATTERN_RECOGNITION = 'COMPUTERS:ALGORITHMS_AND_DATA_STRUCTURES:PATTERN_RECOGNITION', \
                                                                       'Computers:Algorithms_and_Data_Structures:Pattern_Recognition'
        COMPUTERS_ALGORITHMS_AND_DATA_STRUCTURES_DIGITAL_WATERMARKS = 'COMPUTERS:ALGORITHMS_AND_DATA_STRUCTURES:DIGITAL_WATERMARKS', \
                                                                      'Computers:Algorithms_and_Data_Structures:Digital_watermarks'
        COMPUTERS_DATABASES = 'COMPUTERS:DATABASES', 'Computers:Databases'
        COMPUTERS_SECURITY = 'COMPUTERS:SECURITY', 'Computers:Security'
        COMPUTERS_INFORMATION_SYSTEMS = 'COMPUTERS:INFORMATION_SYSTEMS', 'Computers:Information_Systems'
        COMPUTERS_INFORMATION_SYSTEMS_EC_BUSINESSES = 'COMPUTERS:INFORMATION_SYSTEMS:EC_BUSINESSES', \
                                                      'Computers:Information_Systems:EC_businesses'
        COMPUTERS_CYBERNETICS = 'COMPUTERS:CYBERNETICS', 'Computers:Cybernetics'
        COMPUTERS_CYBERNETICS_ARTIFICIAL_INTELLIGENCE = 'COMPUTERS:CYBERNETICS:ARTIFICIAL_INTELLIGENCE', \
                                                        'Computers:Cybernetics:Artificial_Intelligence'
        COMPUTERS_CRYPTOGRAPHY = 'COMPUTERS:CRYPTOGRAPHY', 'Computers:Cryptography'
        COMPUTERS_LECTURES, _MONOGRAPHS = 'COMPUTERS:LECTURES,_MONOGRAPHS', 'Computers:Lectures,_monographs'
        COMPUTERS_MEDIA = 'COMPUTERS:MEDIA', 'Computers:Media'
        COMPUTERS_OPERATING_SYSTEMS = 'COMPUTERS:OPERATING_SYSTEMS', 'Computers:Operating_Systems'
        COMPUTERS_ORGANIZATION_AND_DATA_PROCESSING = 'COMPUTERS:ORGANIZATION_AND_DATA_PROCESSING', \
                                                     'Computers:Organization_and_Data_Processing'
        COMPUTERS_PROGRAMMING = 'COMPUTERS:PROGRAMMING', 'Computers:Programming'
        COMPUTERS_PROGRAMMING_LIBRARIES_API = 'COMPUTERS:PROGRAMMING:LIBRARIES_API', \
                                              'Computers:Programming:Libraries_API'
        COMPUTERS_PROGRAMMING_GAMES = 'COMPUTERS:PROGRAMMING:GAMES', 'Computers:Programming:Games'
        COMPUTERS_PROGRAMMING_COMPILERS = 'COMPUTERS:PROGRAMMING:COMPILERS', 'Computers:Programming:Compilers'
        COMPUTERS_PROGRAMMING_MODELING_LANGUAGES = 'COMPUTERS:PROGRAMMING:MODELING_LANGUAGES', \
                                                   'Computers:Programming:Modeling_languages'
        COMPUTERS_PROGRAMMING_PROGRAMMING_LANGUAGES = 'COMPUTERS:PROGRAMMING:PROGRAMMING_LANGUAGES', \
                                                      'Computers:Programming:Programming_Languages'
        COMPUTERS_PROGRAMS_TEX, _LATEX = 'COMPUTERS:PROGRAMS:TEX,_LATEX', 'Computers:Programs:TeX,_LaTeX'
        COMPUTERS_SOFTWARE_OFFICE_SOFTWARE = 'COMPUTERS:SOFTWARE:OFFICE_SOFTWARE', \
                                             'Computers:Software:Office_software'
        COMPUTERS_SOFTWARE_ADOBE_PRODUCTS = 'COMPUTERS:SOFTWARE:ADOBE_PRODUCTS', 'Computers:Software:Adobe_Products'
        COMPUTERS_SOFTWARE_MACROMEDIA_PRODUCTS = 'COMPUTERS:SOFTWARE:MACROMEDIA_PRODUCTS', \
                                                 'Computers:Software:Macromedia_Products'
        COMPUTERS_SOFTWARE_CAD = 'COMPUTERS:SOFTWARE:CAD', 'Computers:Software:CAD'
        COMPUTERS_SOFTWARE_SYSTEMS_SCIENTIFIC_COMPUTING = 'COMPUTERS:SOFTWARE:SYSTEMS:SCIENTIFIC_COMPUTING', \
                                                          'Computers:Software:Systems:scientific_computing'
        COMPUTERS_NETWORKING = 'COMPUTERS:NETWORKING', 'Computers:Networking'
        COMPUTERS_NETWORKING_INTERNET = 'COMPUTERS:NETWORKING:INTERNET', 'Computers:Networking:Internet'
        COMPUTERS_SYSTEM_ADMINISTRATION = 'COMPUTERS:SYSTEM_ADMINISTRATION', 'Computers:System_Administration'
        LITERATURE = 'LITERATURE', 'Literature'
        LITERATURE_FICTION = 'LITERATURE:FICTION', 'Literature:Fiction'
        LITERATURE_LIBRARY = 'LITERATURE:LIBRARY', 'Literature:Library'
        LITERATURE_DETECTIVE = 'LITERATURE:DETECTIVE', 'Literature:Detective'
        LITERATURE_CHILDREN = 'LITERATURE:CHILDREN', 'Literature:Children'
        LITERATURE_COMICS = 'LITERATURE:COMICS', 'Literature:Comics'
        LITERATURE_LITERARY = 'LITERATURE:LITERARY', 'Literature:Literary'
        LITERATURE_POETRY = 'LITERATURE:POETRY', 'Literature:Poetry'
        LITERATURE_PROSE = 'LITERATURE:PROSE', 'Literature:Prose'
        LITERATURE_FOLKLORE = 'LITERATURE:FOLKLORE', 'Literature:Folklore'
        LITERATURE_FANTASY = 'LITERATURE:FANTASY', 'Literature:Fantasy'
        MATHEMATICS = 'MATHEMATICS', 'Mathematics'
        MATHEMATICS_ALGEBRA = 'MATHEMATICS:ALGEBRA', 'Mathematics:Algebra'
        MATHEMATICS_ALGEBRA_LINEAR_ALGEBRA = 'MATHEMATICS:ALGEBRA:LINEAR_ALGEBRA', \
                                             'Mathematics:Algebra:Linear_Algebra'
        MATHEMATICS_ALGORITHMS_AND_DATA_STRUCTURES = 'MATHEMATICS:ALGORITHMS_AND_DATA_STRUCTURES', \
                                                     'Mathematics:Algorithms_and_Data_Structures'
        MATHEMATICS_ANALYSIS = 'MATHEMATICS:ANALYSIS', 'Mathematics:Analysis'
        MATHEMATICS_WAVELETS_AND_SIGNAL_PROCESSING = 'MATHEMATICS:WAVELETS_AND_SIGNAL_PROCESSING', \
                                                     'Mathematics:Wavelets_and_signal_processing'
        MATHEMATICS_PROBABILITY = 'MATHEMATICS:PROBABILITY', 'Mathematics:Probability'
        MATHEMATICS_COMPUTATIONAL_MATHEMATICS = 'MATHEMATICS:COMPUTATIONAL_MATHEMATICS', \
                                                'Mathematics:Computational_Mathematics'
        MATHEMATICS_GEOMETRY_AND_TOPOLOGY = 'MATHEMATICS:GEOMETRY_AND_TOPOLOGY', 'Mathematics:Geometry_and_Topology'
        MATHEMATICS_PUZZLE = 'MATHEMATICS:PUZZLE', 'Mathematics:Puzzle'
        MATHEMATICS_DYNAMICAL_SYSTEMS = 'MATHEMATICS:DYNAMICAL_SYSTEMS', 'Mathematics:Dynamical_Systems'
        MATHEMATICS_DISCRETE_MATHEMATICS = 'MATHEMATICS:DISCRETE_MATHEMATICS', 'Mathematics:Discrete_Mathematics'
        MATHEMATICS_DIFFERENTIAL_EQUATIONS = 'MATHEMATICS:DIFFERENTIAL_EQUATIONS', 'Mathematics:Differential_Equations'
        MATHEMATICS_COMBINATORICS = 'MATHEMATICS:COMBINATORICS', 'Mathematics:Combinatorics'
        MATHEMATICS_THE_COMPLEX_VARIABLE = 'MATHEMATICS:THE_COMPLEX_VARIABLE', 'Mathematics:The_complex_variable'
        MATHEMATICS_COMPUTER_ALGEBRA = 'MATHEMATICS:COMPUTER_ALGEBRA', 'Mathematics:Computer_Algebra'
        MATHEMATICS_LECTURES = 'MATHEMATICS:LECTURES', 'Mathematics:Lectures'
        MATHEMATICS_LOGIC = 'MATHEMATICS:LOGIC', 'Mathematics:Logic'
        MATHEMATICS_MATHEMATICSEMATICAL_STATISTICS = 'MATHEMATICS:MATHEMATICSEMATICAL_STATISTICS', \
                                                     'Mathematics:Mathematicsematical_Statistics'
        MATHEMATICS_MATHEMATICSEMATICAL_PHYSICS = 'MATHEMATICS:MATHEMATICSEMATICAL_PHYSICS', \
                                                  'Mathematics:Mathematicsematical_Physics'
        MATHEMATICS_CONTINUED_FRACTIONS = 'MATHEMATICS:CONTINUED_FRACTIONS', 'Mathematics:Continued_fractions'
        MATHEMATICS_FUZZY_LOGIC_AND_APPLICATIONS = 'MATHEMATICS:FUZZY_LOGIC_AND_APPLICATIONS', \
                                                   'Mathematics:Fuzzy_Logic_and_Applications'
        MATHEMATICS_OPTIMAL_CONTROL = 'MATHEMATICS:OPTIMAL_CONTROL', 'Mathematics:Optimal_control'
        MATHEMATICS_OPTIMIZATION_OPERATIONS_RESEARCH = 'MATHEMATICS:OPTIMIZATION._OPERATIONS_RESEARCH', \
                                                       'Mathematics:Optimization._Operations_Research'
        MATHEMATICS_APPLIED_MATHEMATICSEMATICS = 'MATHEMATICS:APPLIED_MATHEMATICSEMATICS', \
                                                 'Mathematics:Applied_Mathematicsematics'
        MATHEMATICS_SYMMETRY_AND_GROUP = 'MATHEMATICS:SYMMETRY_AND_GROUP', 'Mathematics:Symmetry_and_group'
        MATHEMATICS_AUTOMATIC_CONTROL_THEORY = 'MATHEMATICS:AUTOMATIC_CONTROL_THEORY', \
                                               'Mathematics:Automatic_Control_Theory'
        MATHEMATICS_GRAPH_THEORY = 'MATHEMATICS:GRAPH_THEORY', 'Mathematics:Graph_Theory'
        MATHEMATICS_GAME_THEORY = 'MATHEMATICS:GAME_THEORY', 'Mathematics:Game_Theory'
        MATHEMATICS_OPERATOR_THEORY = 'MATHEMATICS:OPERATOR_THEORY', 'Mathematics:Operator_Theory'
        MATHEMATICS_NUMBER_THEORY = 'MATHEMATICS:NUMBER_THEORY', 'Mathematics:Number_Theory'
        MATHEMATICS_FUNCTIONAL_ANALYSIS = 'MATHEMATICS:FUNCTIONAL_ANALYSIS', 'Mathematics:Functional_Analysis'
        MATHEMATICS_NUMERICAL_ANALYSIS = 'MATHEMATICS:NUMERICAL_ANALYSIS', 'Mathematics:Numerical_Analysis'
        MATHEMATICS_ELEMENTARY = 'MATHEMATICS:ELEMENTARY', 'Mathematics:Elementary'
        MEDICINE = 'MEDICINE', 'Medicine'
        MEDICINE_ANATOMY_AND_PHYSIOLOGY = 'MEDICINE:ANATOMY_AND_PHYSIOLOGY', 'Medicine:Anatomy_and_physiology'
        MEDICINE_ANESTHESIOLOGY_AND_INTENSIVE_CARE = 'MEDICINE:ANESTHESIOLOGY_AND_INTENSIVE_CARE', \
                                                     'Medicine:Anesthesiology_and_Intensive_Care'
        MEDICINE_DISEASES = 'MEDICINE:DISEASES', 'Medicine:Diseases'
        MEDICINE_DISEASES_INTERNAL_MEDICINE = 'MEDICINE:DISEASES:INTERNAL_MEDICINE', \
                                              'Medicine:Diseases:Internal_Medicine'
        MEDICINE_HISTOLOGY = 'MEDICINE:HISTOLOGY', 'Medicine:Histology'
        MEDICINE_HOMEOPATHY = 'MEDICINE:HOMEOPATHY', 'Medicine:Homeopathy'
        MEDICINE_DERMATOLOGY = 'MEDICINE:DERMATOLOGY', 'Medicine:Dermatology'
        MEDICINE_DIABETES = 'MEDICINE:DIABETES', 'Medicine:Diabetes'
        MEDICINE_IMMUNOLOGY = 'MEDICINE:IMMUNOLOGY', 'Medicine:immunology'
        MEDICINE_INFECTIOUS_DISEASES = 'MEDICINE:INFECTIOUS_DISEASES', 'Medicine:Infectious_diseases'
        MEDICINE_YOGA = 'MEDICINE:YOGA', 'Medicine:Yoga'
        MEDICINE_CARDIOLOGY = 'MEDICINE:CARDIOLOGY', 'Medicine:Cardiology'
        MEDICINE_CHINESE_MEDICINE = 'MEDICINE:CHINESE_MEDICINE', 'Medicine:Chinese_Medicine'
        MEDICINE_CLINICAL_MEDICINE = 'MEDICINE:CLINICAL_MEDICINE', 'Medicine:Clinical_Medicine'
        MEDICINE_MOLECULAR_MEDICINE = 'MEDICINE:MOLECULAR_MEDICINE', 'Medicine:Molecular_Medicine'
        MEDICINE_NATURAL_MEDICINE = 'MEDICINE:NATURAL_MEDICINE', 'Medicine:Natural_Medicine'
        MEDICINE_POPULAR_SCIENTIFIC_LITERATURE = 'MEDICINE:POPULAR_SCIENTIFIC_LITERATURE', \
                                                 'Medicine:Popular_scientific_literature'
        MEDICINE_NEUROLOGY = 'MEDICINE:NEUROLOGY', 'Medicine:Neurology'
        MEDICINE_ONCOLOGY = 'MEDICINE:ONCOLOGY', 'Medicine:Oncology'
        MEDICINE_ENT = 'MEDICINE:ENT', 'Medicine:ENT'
        MEDICINE_OPHTHALMOLOGY = 'MEDICINE:OPHTHALMOLOGY', 'Medicine:Ophthalmology'
        MEDICINE_PEDIATRICS = 'MEDICINE:PEDIATRICS', 'Medicine:Pediatrics'
        MEDICINE_DENTISTRY, _ORTHODONTICS = 'MEDICINE:DENTISTRY,_ORTHODONTICS', 'Medicine:Dentistry,_Orthodontics'
        MEDICINE_TRIAL = 'MEDICINE:TRIAL', 'Medicine:Trial'
        MEDICINE_THERAPY = 'MEDICINE:THERAPY', 'Medicine:Therapy'
        MEDICINE_PHARMACOLOGY = 'MEDICINE:PHARMACOLOGY', 'Medicine:Pharmacology'
        MEDICINE_FENG_SHUI = 'MEDICINE:FENG_SHUI', 'Medicine:Feng_Shui'
        MEDICINE_SURGERY, _ORTHOPEDICS = 'MEDICINE:SURGERY,_ORTHOPEDICS', 'Medicine:Surgery,_Orthopedics'
        MEDICINE_ENDOCRINOLOGY = 'MEDICINE:ENDOCRINOLOGY', 'Medicine:Endocrinology'
        MEDICINE_EPIDEMIOLOGY = 'MEDICINE:EPIDEMIOLOGY', 'Medicine:Epidemiology'
        SCIENCE_GENERAL = 'SCIENCE_(GENERAL)', 'Science_(General)'
        SCIENCE_GENERAL_INTERNATIONAL_CONFERENCES_AND_SYMPOSIUMS = 'SCIENCE_(GENERAL):INTERNATIONAL_CONFERENCES_AND_SYMPOSIUMS', \
                                                                   'Science_(general):International_Conferences_and_Symposiums'
        SCIENCE_GENERAL_SCIENCE_OF_SCIENCE = 'SCIENCE_(GENERAL):SCIENCE_OF_SCIENCE', \
                                             'Science_(general):Science_of_Science'
        SCIENCE_GENERAL_SCIENTIFIC_POPULAR = 'SCIENCE_(GENERAL):SCIENTIFIC-POPULAR', \
                                             'Science_(general):Scientific-popular'
        SCIENCE_GENERAL_SCIENTIFIC_AND_POPULAR_JOURNALISM = 'SCIENCE_(GENERAL):SCIENTIFIC_AND_POPULAR:JOURNALISM', \
                                                            'Science_(general):Scientific_and_popular:Journalism'
        EDUCATION = 'EDUCATION', 'Education'
        EDUCATION_THESES_ABSTRACTS = 'EDUCATION:THESES_ABSTRACTS', 'Education:Theses_abstracts'
        EDUCATION_INTERNATIONAL_CONFERENCES_AND_SYMPOSIUMS = 'EDUCATION:INTERNATIONAL_CONFERENCES_AND_SYMPOSIUMS', \
                                                             'Education:International_Conferences_and_Symposiums'
        EDUCATION_SELF_HELP_BOOKS = 'EDUCATION:SELF_HELP_BOOKS', 'Education:self_help_books'
        EDUCATION_ELEMENTARY = 'EDUCATION:ELEMENTARY', 'Education:Elementary'
        EDUCATION_ENCYCLOPEDIA = 'EDUCATION:ENCYCLOPEDIA', 'Education:Encyclopedia'
        OTHER_SOCIAL_SCIENCES = 'OTHER_SOCIAL_SCIENCES', 'Other_Social_Sciences'
        OTHER_SOCIAL_SCIENCES_JOURNALISM, _MEDIA = 'OTHER_SOCIAL_SCIENCES:JOURNALISM,_MEDIA', \
                                                   'Other_Social_Sciences:Journalism,_Media'
        OTHER_SOCIAL_SCIENCES_CULTURAL = 'OTHER_SOCIAL_SCIENCES:CULTURAL', 'Other_Social_Sciences:Cultural'
        OTHER_SOCIAL_SCIENCES_POLITICS = 'OTHER_SOCIAL_SCIENCES:POLITICS', 'Other_Social_Sciences:Politics'
        OTHER_SOCIAL_SCIENCES_POLITICS_INTERNATIONAL_RELATIONS = 'OTHER_SOCIAL_SCIENCES:POLITICS:INTERNATIONAL_RELATIONS', \
                                                                 'Other_Social_Sciences:Politics:International_Relations'
        OTHER_SOCIAL_SCIENCES_SOCIOLOGY = 'OTHER_SOCIAL_SCIENCES:SOCIOLOGY', 'Other_Social_Sciences:Sociology'
        OTHER_SOCIAL_SCIENCES_PHILOSOPHY = 'OTHER_SOCIAL_SCIENCES:PHILOSOPHY', 'Other_Social_Sciences:Philosophy'
        OTHER_SOCIAL_SCIENCES_PHILOSOPHY_CRITICAL_THINKING = 'OTHER_SOCIAL_SCIENCES:PHILOSOPHY:CRITICAL_THINKING', \
                                                             'Other_Social_Sciences:Philosophy:Critical_Thinking'
        OTHER_SOCIAL_SCIENCES_ETHNOGRAPHY = 'OTHER_SOCIAL_SCIENCES:ETHNOGRAPHY', 'Other_Social_Sciences:Ethnography'
        PSYCHOLOGY = 'PSYCHOLOGY', 'Psychology'
        PSYCHOLOGY_HYPNOSIS = 'PSYCHOLOGY:HYPNOSIS', 'Psychology:Hypnosis'
        PSYCHOLOGY_THE_ART_OF_COMMUNICATION = 'PSYCHOLOGY:THE_ART_OF_COMMUNICATION', \
                                              'Psychology:The_art_of_communication'
        PSYCHOLOGY_LOVE, _EROTIC = 'PSYCHOLOGY:LOVE,_EROTIC', 'Psychology:Love,_erotic'
        PSYCHOLOGY_NEURO_LINGUISTIC_PROGRAMMING = 'PSYCHOLOGY:NEURO_LINGUISTIC_PROGRAMMING', \
                                                  'Psychology:Neuro_Linguistic_Programming'
        PSYCHOLOGY_PEDAGOGY = 'PSYCHOLOGY:PEDAGOGY', 'Psychology:Pedagogy'
        PSYCHOLOGY_CREATIVE_THINKING = 'PSYCHOLOGY:CREATIVE_THINKING', 'Psychology:Creative_Thinking'
        RELIGION = 'RELIGION', 'Religion'
        RELIGION_BUDDHISM = 'RELIGION:BUDDHISM', 'Religion:Buddhism'
        RELIGION_KABBALAH = 'RELIGION:KABBALAH', 'Religion:kabbalah'
        RELIGION_ORTHODOXY = 'RELIGION:ORTHODOXY', 'Religion:Orthodoxy'
        RELIGION_ESOTERIC, _MYSTERY = 'RELIGION:ESOTERIC,_MYSTERY', 'Religion:Esoteric,_Mystery'
        TECHNIQUE = 'TECHNIQUE', 'Technique'
        TECHNIQUE_AUTOMATION = 'TECHNIQUE:AUTOMATION', 'Technique:Automation'
        TECHNIQUE_AEROSPACE_EQUIPMENT = 'TECHNIQUE:AEROSPACE_EQUIPMENT', 'Technique:Aerospace_Equipment'
        TECHNIQUE_WATER_TREATMENT = 'TECHNIQUE:WATER_TREATMENT', 'Technique:Water_Treatment'
        TECHNIQUE_MILITARY_EQUIPMENT = 'TECHNIQUE:MILITARY_EQUIPMENT', 'Technique:Military_equipment'
        TECHNIQUE_MILITARY_EQUIPMENT_WEAPON = 'TECHNIQUE:MILITARY_EQUIPMENT:WEAPON', \
                                              'Technique:Military_equipment:Weapon'
        TECHNIQUE_PUBLISHING = 'TECHNIQUE:PUBLISHING', 'Technique:Publishing'
        TECHNOLOGY_SPACE_SCIENCE = 'TECHNOLOGY:SPACE_SCIENCE', 'Technology:Space_Science'
        TECHNIQUE_LIGHT_INDUSTRY = 'TECHNIQUE:LIGHT_INDUSTRY', 'Technique:Light_Industry'
        TECHNIQUE_MATERIALS = 'TECHNIQUE:MATERIALS', 'Technique:Materials'
        TECHNOLOGY_MECHANICAL_ENGINEERING = 'TECHNOLOGY:MECHANICAL_ENGINEERING', 'Technology:Mechanical_Engineering'
        TECHNIQUE_METALLURGY = 'TECHNIQUE:METALLURGY', 'Technique:Metallurgy'
        TECHNIQUE_METROLOGY = 'TECHNIQUE:METROLOGY', 'Technique:Metrology'
        TECHNIQUE_SAFETY_AND_SECURITY = 'TECHNIQUE:SAFETY_AND_SECURITY', 'Technique:Safety_and_Security'
        TECHNIQUE_NANOTECHNOLOGY = 'TECHNIQUE:NANOTECHNOLOGY', 'Technique:Nanotechnology'
        TECHNIQUE_OIL_AND_GAS_TECHNOLOGIES = 'TECHNIQUE:OIL_AND_GAS_TECHNOLOGIES', 'Technique:Oil_and_Gas_Technologies'
        TECHNIQUE_OIL_AND_GAS_TECHNOLOGIES_PIPELINES = 'TECHNIQUE:OIL_AND_GAS_TECHNOLOGIES:PIPELINES', \
                                                       'Technique:Oil_and_Gas_Technologies:Pipelines'
        TECHNIQUE_REGULATORY_LITERATURE = 'TECHNIQUE:REGULATORY_LITERATURE', 'Technique:Regulatory_Literature'
        TECHNIQUE_PATENT_BUSINESS_INGENUITY_INNOVATION = 'TECHNIQUE:PATENT_BUSINESS._INGENUITY._INNOVATION', \
                                                         'Technique:Patent_Business._Ingenuity._Innovation'
        TECHNIQUE_FOOD_MANUFACTURING = 'TECHNIQUE:FOOD_MANUFACTURING', 'Technique:Food_Manufacturing'
        TECHNIQUE_INSTRUMENT = 'TECHNIQUE:INSTRUMENT', 'Technique:Instrument'
        TECHNIQUE_INDUSTRY_METALLURGY = 'TECHNIQUE:INDUSTRY:METALLURGY', 'Technique:Industry:Metallurgy'
        TECHNIQUE_INDUSTRIAL_EQUIPMENT_AND_TECHNOLOGY = 'TECHNIQUE:INDUSTRIAL_EQUIPMENT_AND_TECHNOLOGY', \
                                                        'Technique:industrial_equipment_and_technology'
        TECHNIQUE_MISSILES = 'TECHNIQUE:MISSILES', 'Technique:Missiles'
        TECHNIQUE_COMMUNICATION = 'TECHNIQUE:COMMUNICATION', 'Technique:Communication'
        TECHNIQUE_COMMUNICATION_TELECOMMUNICATIONS = 'TECHNIQUE:COMMUNICATION:TELECOMMUNICATIONS', \
                                                     'Technique:Communication:Telecommunications'
        TECHNIQUE_CONSTRUCTION = 'TECHNIQUE:CONSTRUCTION', 'Technique:Construction'
        TECHNIQUE_CONSTRUCTION_VENTILATION_AND_AIR_CONDITIONING = 'TECHNIQUE:CONSTRUCTION:VENTILATION_AND_AIR_CONDITIONING', \
                                                                  'Technique:Construction:Ventilation_and_Air_Conditioning'
        TECHNIQUE_CONSTRUCTION_RENOVATION_AND_INTERIOR_DESIGN = 'TECHNIQUE:CONSTRUCTION:RENOVATION_AND_INTERIOR_DESIGN', \
                                                                'Technique:Construction:Renovation_and_interior_design'
        TECHNIQUE_CONSTRUCTION_RENOVATION_AND_INTERIOR_DESIGN_SAUNAS = 'TECHNIQUE:CONSTRUCTION:RENOVATION_AND_INTERIOR_DESIGN:SAUNAS', \
                                                                       'Technique:Construction:Renovation_and_interior_design:Saunas'
        TECHNIQUE_CONSTRUCTION_CEMENT_INDUSTRY = 'TECHNIQUE:CONSTRUCTION:CEMENT_INDUSTRY', \
                                                 'Technique:Construction:Cement_Industry'
        TECHNIQUE_HEAT = 'TECHNIQUE:HEAT', 'Technique:Heat'
        TECHNIQUE_FUEL_TECHNOLOGY = 'TECHNIQUE:FUEL_TECHNOLOGY', 'Technique:Fuel_Technology'
        TECHNIQUE_TRANSPORT = 'TECHNIQUE:TRANSPORT', 'Technique:Transport'
        TECHNIQUE_TRANSPORTATION_AVIATION = 'TECHNIQUE:TRANSPORTATION:AVIATION', 'Technique:Transportation:Aviation'
        TECHNIQUE_TRANSPORTATION_CARS, _MOTORCYCLES = 'TECHNIQUE:TRANSPORTATION:CARS,_MOTORCYCLES', \
                                                      'Technique:Transportation:Cars,_motorcycles'
        TECHNIQUE_TRANSPORTATION_RAIL = 'TECHNIQUE:TRANSPORTATION:RAIL', 'Technique:Transportation:Rail'
        TECHNIQUE_TRANSPORTATION_SHIPS = 'TECHNIQUE:TRANSPORTATION:SHIPS', 'Technique:Transportation:Ships'
        TECHNIQUE_REFRIGERATION = 'TECHNIQUE:REFRIGERATION', 'Technique:Refrigeration'
        TECHNIQUE_ELECTRONICS = 'TECHNIQUE:ELECTRONICS', 'Technique:Electronics'
        TECHNIQUE_ELECTRONICS_HARDWARE = 'TECHNIQUE:ELECTRONICS:HARDWARE', 'Technique:Electronics:Hardware'
        TECHNIQUE_ELECTRONICS_FIBER_OPTICS = 'TECHNIQUE:ELECTRONICS:FIBER_OPTICS', \
                                             'Technique:Electronics:Fiber_Optics'
        TECHNIQUE_ELECTRONICS_HOME_ELECTRONICS = 'TECHNIQUE:ELECTRONICS:HOME_ELECTRONICS', \
                                                 'Technique:Electronics:Home_Electronics'
        TECHNIQUE_ELECTRONICS_MICROPROCESSOR_TECHNOLOGY = 'TECHNIQUE:ELECTRONICS:MICROPROCESSOR_TECHNOLOGY', \
                                                          'Technique:Electronics:Microprocessor_Technology'
        TECHNIQUE_ELECTRONICS_SIGNAL_PROCESSING = 'TECHNIQUE:ELECTRONICS:SIGNAL_PROCESSING', \
                                                  'Technique:Electronics:Signal_Processing'
        TECHNIQUE_ELECTRONICS_RADIO = 'TECHNIQUE:ELECTRONICS:RADIO', 'Technique:Electronics:Radio'
        TECHNIQUE_ELECTRONICS_ROBOTICS = 'TECHNIQUE:ELECTRONICS:ROBOTICS', 'Technique:Electronics:Robotics'
        TECHNIQUE_ELECTRONICS_VLSI = 'TECHNIQUE:ELECTRONICS:VLSI', 'Technique:Electronics:VLSI'
        TECHNIQUE_ELECTRONICS_TV_VIDEO = 'TECHNIQUE:ELECTRONICS:TV._VIDEO', 'Technique:Electronics:TV._Video'
        TECHNIQUE_ELECTRONICS_TELECOMMUNICATIONS = 'TECHNIQUE:ELECTRONICS:TELECOMMUNICATIONS', \
                                                   'Technique:Electronics:Telecommunications'
        TECHNIQUE_ELECTRONICS_ELECTRONICS = 'TECHNIQUE:ELECTRONICS:ELECTRONICS', 'Technique:Electronics:Electronics'
        TECHNIQUE_ENERGY = 'TECHNIQUE:ENERGY', 'Technique:Energy'
        TECHNIQUE_ENERGY_RENEWABLE_ENERGY = 'TECHNIQUE:ENERGY:RENEWABLE_ENERGY', 'Technique:Energy:Renewable_Energy'
        PHYSICS = 'PHYSICS', 'Physics'
        PHYSICS_ASTRONOMY = 'PHYSICS:ASTRONOMY', 'Physics:Astronomy'
        PHYSICS_ASTRONOMY_ASTROPHYSICS = 'PHYSICS:ASTRONOMY:ASTROPHYSICS', 'Physics:Astronomy:Astrophysics'
        PHYSICS_GEOPHYSICS = 'PHYSICS:GEOPHYSICS', 'Physics:Geophysics'
        PHYSICS_QUANTUM_MECHANICS = 'PHYSICS:QUANTUM_MECHANICS', 'Physics:Quantum_Mechanics'
        PHYSICS_QUANTUM_PHYSICS = 'PHYSICS:QUANTUM_PHYSICS', 'Physics:Quantum_Physics'
        PHYSICS_CRYSTAL_PHYSICS = 'PHYSICS:CRYSTAL_PHYSICS', 'Physics:Crystal_Physics'
        PHYSICS_MECHANICS = 'PHYSICS:MECHANICS', 'Physics:Mechanics'
        PHYSICS_MECHANICS_OSCILLATIONS_AND_WAVES = 'PHYSICS:MECHANICS:OSCILLATIONS_AND_WAVES', \
                                                   'Physics:Mechanics:Oscillations_and_Waves'
        PHYSICS_MECHANICS_MECHANICS_OF_DEFORMABLE_BODIES = 'PHYSICS:MECHANICS:MECHANICS_OF_DEFORMABLE_BODIES', \
                                                           'Physics:Mechanics:Mechanics_of_deformable_bodies'
        PHYSICS_MECHANICS_FLUID_MECHANICS = 'PHYSICS:MECHANICS:FLUID_MECHANICS', 'Physics:Mechanics:Fluid_Mechanics'
        PHYSICS_MECHANICS_NONLINEAR_DYNAMICS_AND_CHAOS = 'PHYSICS:MECHANICS:NONLINEAR_DYNAMICS_AND_CHAOS', \
                                                         'Physics:Mechanics:Nonlinear_dynamics_and_chaos'
        PHYSICS_MECHANICS_STRENGTH_OF_MATERIALS = 'PHYSICS:MECHANICS:STRENGTH_OF_MATERIALS', \
                                                  'Physics:Mechanics:Strength_of_Materials'
        PHYSICS_MECHANICS_THEORY_OF_ELASTICITY = 'PHYSICS:MECHANICS:THEORY_OF_ELASTICITY', \
                                                 'Physics:Mechanics:Theory_of_Elasticity'
        PHYSICS_GENERAL_COURSES = 'PHYSICS:GENERAL_COURSES', 'Physics:General_courses'
        PHYSICS_OPTICS = 'PHYSICS:OPTICS', 'Physics:Optics'
        PHYSICS_SPECTROSCOPY = 'PHYSICS:SPECTROSCOPY', 'Physics:Spectroscopy'
        PHYSICS_THEORY_OF_RELATIVITY_AND_GRAVITATION = 'PHYSICS:THEORY_OF_RELATIVITY_AND_GRAVITATION', \
                                                       'Physics:Theory_of_Relativity_and_Gravitation'
        PHYSICS_THERMODYNAMICS_AND_STATISTICAL_MECHANICS = 'PHYSICS:THERMODYNAMICS_AND_STATISTICAL_MECHANICS', \
                                                           'Physics:Thermodynamics_and_Statistical_Mechanics'
        PHYSICS_PHYSICS_OF_THE_ATMOSPHERE = 'PHYSICS:PHYSICS_OF_THE_ATMOSPHERE', 'Physics:Physics_of_the_Atmosphere'
        PHYSICS_PHYSICS_OF_LASERS = 'PHYSICS:PHYSICS_OF_LASERS', 'Physics:Physics_of_lasers'
        PHYSICS_PLASMA_PHYSICS = 'PHYSICS:PLASMA_PHYSICS', 'Physics:Plasma_Physics'
        PHYSICS_SOLID_STATE_PHYSICS = 'PHYSICS:SOLID_STATE_PHYSICS', 'Physics:Solid_State_Physics'
        PHYSICS_ELECTRICITY_AND_MAGNETISM = 'PHYSICS:ELECTRICITY_AND_MAGNETISM', 'Physics:Electricity_and_Magnetism'
        PHYSICS_ELECTRODYNAMICS = 'PHYSICS:ELECTRODYNAMICS', 'Physics:Electrodynamics'
        PHYSICAL_EDUCATION_AND_SPORT = 'PHYSICAL_EDUCATION_AND_SPORT', 'Physical_Education_and_Sport'
        PHYSICAL_EDUCATION_AND_SPORT_BODYBUILDING = 'PHYSICAL_EDUCATION_AND_SPORT:BODYBUILDING', \
                                                    'Physical_education_and_sport:Bodybuilding'
        PHYSICAL_EDUCATION_AND_SPORT_MARTIAL_ARTS = 'PHYSICAL_EDUCATION_AND_SPORT:MARTIAL_ARTS', \
                                                    'Physical_education_and_sport:Martial_Arts'
        PHYSICAL_EDUCATION_AND_SPORT_BIKE = 'PHYSICAL_EDUCATION_AND_SPORT:BIKE', 'Physical_education_and_sport:Bike'
        PHYSICAL_EDUCATION_AND_SPORT_SURVIVAL = 'PHYSICAL_EDUCATION_AND_SPORT:SURVIVAL', \
                                                'Physical_education_and_sport:Survival'
        PHYSICAL_EDUCATION_AND_SPORT_SPORT_FISHING = 'PHYSICAL_EDUCATION_AND_SPORT:SPORT_FISHING', \
                                                     'Physical_Education_and_Sport:Sport_fishing'
        PHYSICAL_EDUCATION_AND_SPORT_FENCING = 'PHYSICAL_EDUCATION_AND_SPORT:FENCING', \
                                               'Physical_education_and_sport:Fencing'
        CHEMISTRY = 'CHEMISTRY', 'Chemistry'
        CHEMISTRY_ANALYTICAL_CHEMISTRY = 'CHEMISTRY:ANALYTICAL_CHEMISTRY', 'Chemistry:Analytical_Chemistry'
        CHEMISTRY_MATERIALS = 'CHEMISTRY:MATERIALS', 'Chemistry:Materials'
        CHEMISTRY_INORGANIC_CHEMISTRY = 'CHEMISTRY:INORGANIC_CHEMISTRY', 'Chemistry:Inorganic_Chemistry'
        CHEMISTRY_ORGANIC_CHEMISTRY = 'CHEMISTRY:ORGANIC_CHEMISTRY', 'Chemistry:Organic_Chemistry'
        CHEMISTRY_PYROTECHNICS_AND_EXPLOSIVES = 'CHEMISTRY:PYROTECHNICS_AND_EXPLOSIVES', \
                                                'Chemistry:Pyrotechnics_and_explosives'
        CHEMISTRY_PHARMACOLOGY = 'CHEMISTRY:PHARMACOLOGY', 'Chemistry:Pharmacology'
        CHEMISTRY_PHYSICAL_CHEMISTRY = 'CHEMISTRY:PHYSICAL_CHEMISTRY', 'Chemistry:Physical_Chemistry'
        CHEMISTRY_CHEMICAL = 'CHEMISTRY:CHEMICAL', 'Chemistry:Chemical'
        ECONOMY = 'ECONOMY', 'Economy'
        ECONOMY_INVESTING = 'ECONOMY:INVESTING', 'Economy:Investing'
        ECONOMY_MATHEMATICAL_ECONOMICS = 'ECONOMY:MATHEMATICAL_ECONOMICS', 'Economy:Mathematical_Economics'
        ECONOMY_POPULAR = 'ECONOMY:POPULAR', 'Economy:Popular'
        ECONOMY_MARKETS = 'ECONOMY:MARKETS', 'Economy:Markets'
        ECONOMY_ECONOMETRICS = 'ECONOMY:ECONOMETRICS', 'Economy:Econometrics'
        JURISPRUDENCE_CRIMINOLOGY, _FORENSIC_SCIENCE = 'JURISPRUDENCE:CRIMINOLOGY,_FORENSIC_SCIENCE', \
                                                       'Jurisprudence:Criminology,_Forensic_Science'
        JURISPRUDENCE_CRIMINOLOGY_COURT_EXAMINATION = 'JURISPRUDENCE:CRIMINOLOGY:COURT._EXAMINATION', \
                                                      'Jurisprudence:Criminology:Court._examination'
        JURISPRUDENCE_LAW = 'JURISPRUDENCE:LAW', 'Jurisprudence:Law'
        LINGUISTICS = 'LINGUISTICS', 'Linguistics'
        LINGUISTICS_FOREIGN = 'LINGUISTICS:FOREIGN', 'Linguistics:Foreign'
        LINGUISTICS_FOREIGN_ENGLISH = 'LINGUISTICS:FOREIGN:ENGLISH', 'Linguistics:Foreign:English'
        LINGUISTICS_FOREIGN_FRENCH = 'LINGUISTICS:FOREIGN:FRENCH', 'Linguistics:Foreign:French'
        LINGUISTICS_COMPARATIVE_STUDIES = 'LINGUISTICS:COMPARATIVE_STUDIES', 'Linguistics:Comparative_Studies'
        LINGUISTICS_LINGUISTICS = 'LINGUISTICS:LINGUISTICS', 'Linguistics:Linguistics'
        LINGUISTICS_RHETORIC = 'LINGUISTICS:RHETORIC', 'Linguistics:Rhetoric'
        LINGUISTICS_RUSSIAN_LANGUAGE = 'LINGUISTICS:RUSSIAN_LANGUAGE', 'Linguistics:Russian_Language'
        LINGUISTICS_DICTIONARIES = 'LINGUISTICS:DICTIONARIES', 'Linguistics:Dictionaries'
        LINGUISTICS_STYLISTICS = 'LINGUISTICS:STYLISTICS', 'Linguistics:Stylistics'
        OTHERS = 'OTHERS', 'Others'

    class Extensions(models.TextChoices):
        PDF = 'pdf', 'PDF'
        EPUB = 'epub', 'EPUB'

    title = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, unique='identifier', null=True)

    def cover_url(self):
        return self.slug

    description = models.TextField(null=True, blank=True)
    series = models.CharField(max_length=300, null=True, blank=True)
    author = models.ManyToManyField(Author, related_name='published_books')
    year = models.IntegerField(null=True, validators=[MinValueValidator(1800), MaxValueValidator(2100)], blank=True)
    edition = models.CharField(max_length=100, blank=True)
    publisher = models.ManyToManyField(Publisher, related_name='published_books')
    pages = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    language = models.CharField(max_length=50, choices=Languages.choices, default=Languages.ENGLISH)
    topic = models.CharField(max_length=100, choices=Topics.choices, default=Topics.OTHERS)
    cover = models.ImageField(upload_to='covers', name=slug, null=True, blank=True)  # TODO: name of cover = slug
    identifier = models.CharField(max_length=300, blank=True)
    filesize = models.IntegerField(validators=[MinValueValidator(0)])
    extension = models.CharField(max_length=50, choices=Extensions.choices, default=Extensions.PDF)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title
