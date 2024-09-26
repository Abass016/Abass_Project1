# this will contain the questions array

subject_done = []
score = 0
def Biology():
    
    biology_questions = [
    {"question": "1. What is the basic unit of life?", "options": ["A. Atom", "B. Molecule", "C. Cell", "D. Tissue"], "answer": "C"},
    {"question": "2. Which organ in the human body is primarily responsible for pumping blood?", "options": ["A. Brain", "B. Liver", "C. Kidney", "D. Heart"], "answer": "D"},
    {"question": "3. What is the process by which plants make their food?", "options": ["A. Respiration", "B. Photosynthesis", "C. Digestion", "D. Transpiration"], "answer": "B"},
    {"question": "4. What type of cell division results in two identical daughter cells?", "options": ["A. Meiosis", "B. Mitosis", "C. Binary fission", "D. Budding"], "answer": "B"},
    {"question": "5. What is the term for an organism that makes its own food?", "options": ["A. Heterotroph", "B. Autotroph", "C. Carnivore", "D. Omnivore"], "answer": "B"},
    {"question": "6. Which part of the cell contains genetic material?", "options": ["A. Cytoplasm", "B. Mitochondria", "C. Nucleus", "D. Ribosome"], "answer": "C"},
    {"question": "7. What is the primary function of the respiratory system?", "options": ["A. Digestion", "B. Blood circulation", "C. Gas exchange", "D. Nutrient absorption"], "answer": "C"},
    {"question": "8. What is the name of the pigment responsible for photosynthesis?", "options": ["A. Chlorophyll", "B. Hemoglobin", "C. Melanin", "D. Carotene"], "answer": "A"},
    {"question": "9. Which organ is responsible for producing insulin?", "options": ["A. Heart", "B. Liver", "C. Pancreas", "D. Kidney"], "answer": "C"},
    {"question": "10. What type of organism is yeast?", "options": ["A. Bacteria", "B. Fungus", "C. Protist", "D. Plant"], "answer": "B"},
    {"question": "11. What is the basic unit of life?", "options": ["A.Cell", "B.Tissue", "C.Organ", "D.Organism"], "answer": "A"},
    {"question": "12. Which organelle is known as the powerhouse of the cell?", "options": ["A.Mitochondria", "B.Nucleus", "C. Ribosome", "D.Endoplasmic Reticulum"], "answer": "A"},
    {"question": "13. What is the genetic material in all living organisms?", "options": ["A.Lipids", "B.RNA", "C.Proteins", "D.DNA"], "answer": "D"},
    {"question": "14. What process do plants use to convert sunlight into food?", "options": ["A.Respiration", "B.Photosynthesis", "C.Digestion", "D.Fermentation"], "answer": "B"},
    {"question": "15. Which part of the cell contains the genetic blueprint?", "options": ["A.Cell membrane", "B.Cytoplasm", "C.Nucleus", "D.Mitochondria"], "answer": "C"},
    {"question": "16. What is the primary function of the ribosome?", "options": ["A.Cell division", "B.Energy Production", "C.Photosynthesis", "D.Protein synthesis"], "answer": "D"},
    {"question": "17. Which type of cell division is responsible for growth and repair in multicellular organisms?", "options": ["A.Meiosis", "B.Mitosis", "C.Binary Fission", "D.Budding"], "answer": "B"},
    {"question": "18. What is the term for a change in the DNA sequence of an organism?", "options": ["A.Replication", "B.Transcription", "C.Mutation", "D.Translation"], "answer": "C"},
    {"question": "19. What is the role of chlorophyll in plants?", "options": ["A.Water Transpiration", "B.Absorbing Light Energy", "C.Nutrient Absorption", "D.Cell Division"], "answer": "B"},
    {"question": "20. Which process converts glucose and oxygen into carbon dioxide, water, and energy?", "options": ["A.Cellular Respiration", "B.Photosynthesis", "C.Fermentation", "D.Transcription"], "answer": "A"},
    {"question": "21. What structure in the cell is selectively permeable and controls the movement of substances in and out of the cell?", "options": ["A.Nucleus", "B.Cell Membrane", "C.Cytoplasm", "D.Ribosome"], "answer": "B"},
    {"question": "22. Which of the following is a prokaryotic organism?", "options": ["A.Fungal Cell", "B.Plant Cell", "C.Animal Cell", "D.Bacterium"], "answer": "D"},
    {"question": "23. In which phase of the cell cycle does DNA replication occur?", "options": ["A.Interphase", "B.Prophase", "C.Metaphase", "D.Telophase"], "answer": "A"},
    {"question": "24. What is the term for the variety of different types of organisms in a given area?", "options": ["A.Biodiversity", "B.Ecosystem", "C.Habitat", "D.Biome"], "answer": "A"},
    {"question": "25. Which type of RNA carries genetic information from the nucleus to the ribosome?", "options": ["A.mRNA", "B.tRNA", "C.rRNA", "D.snRNA"], "answer": "A"},
    {"question": "26. What is the name of the process by which cells convert nutrients into energy?", "options": ["A.Metabolism", "B.Digestion", "C.Photosynthesis", "D.Respiration"], "answer": "A"},
    {"question": "27. What is the process by which cells break down glucose to produce energy without oxygen?", "options": ["A.Fermentation", "B.Aerobic Respiration", "C.Photosynthesis", "D.Krebs Cycle"], "answer": "A"},
    {"question": "28. What is the main function of the cell wall in plant cells?", "options": ["A.Structural Support", "B.Photosynthesis", "C.Energy Production", "D.Transport"], "answer": "A"},
    {"question": "29. Which type of genetic cross involves two traits?", "options": ["A.Dihybrid Cross", "B.Monohybrid Cross", "C.Back Cross", "D.Test Cross"], "answer": "A"},
    {"question": "30. What is the primary role of the mitochondria?", "options": ["A.Energy Production", "B.Protein Synthesis", "C.Genetic Material Storage", "D.Cell Division"], "answer": "A"},
    {"question": "31. What term describes the process by which organisms with advantageous traits are more likely to survive and reproduce?", "options": ["A.Natural Selection", "B.Genetic Drift", "C.Mutation", "D.Gene Flow"], "answer": "A"},
    {"question": "32. Which scientist is known for developing the theory of evolution by natural selection?", "options": ["A.Charles Darwin", "B.Gregor Mendel", "C.Louis Pasteur", "D.James Watson"], "answer": "A"},
    {"question": "33. What is the term for the genetic makeup of an organism?", "options": ["A.Genotype", "B.Phenotype", "C.Chromosome", "D.Allele"], "answer": "A"},
    {"question": "34. Which process results in the formation of gametes?", "options": ["A.Meiosis", "B.Mitosis", "C.Binary Fission", "D.Budding"], "answer": "A"},
    {"question": "35. What is the role of the endoplasmic reticulum?", "options": ["A.Protein and Lipid Synthesis", "B.Energy Production", "C.Waste Removal", "D.Genetic Material Storage"], "answer": "A"},
    {"question": "36. What is the term for the observable traits of an organism?", "options": ["A.Phenotype", "B.Genotype", "C.Genome", "D.Karyotype"], "answer": "A"},
    {"question": "37. Which organelle is involved in the synthesis of lipids and steroids?", "options": ["A.Smooth Endoplasmic Reticulum", "B.Rough Endoplasmic Reticulum", "C.Golgi Apparatus", "D.Mitochondria"], "answer": "A"},
    {"question": "38. What is the term for the movement of molecules from an area of high concentration to an area of low concentration?", "options": ["A.Diffusion", "B.Osmosis", "C.Active Transport", "D.Facilitated Diffusion"], "answer": "A"},
    {"question": "39. What is the purpose of cellular respiration?", "options": ["A.To produce ATP", "B.To synthesize proteins", "C.To replicate DNA", "D.To perform photosynthesis"], "answer": "A"},
    {"question": "40. What term describes a cell with a full set of chromosomes?", "options": ["A.Diploid", "B.Haploid", "C.Monoploid", "D.Triploid"], "answer": "A"},
    {"question": "41. Which process involves the division of the cytoplasm during cell division?", "options": ["A.Cytokinesis", "B.Mitosis", "C.Meiosis", "D.Interphase"], "answer": "A"},
    {"question": "42. What is the function of the Golgi apparatus?", "options": ["A.Protein Modification and Packaging", "B.DNA Replication", "C.Energy Production", "D.Cell Wall Formation"], "answer": "A"},
    {"question": "43. Which phase of mitosis involves the alignment of chromosomes at the cell's equatorial plane?", "options": ["A.Metaphase", "B.Anaphase", "C.Telophase", "D.Prophase"], "answer": "A"},
    {"question": "44. What term describes the total of all chemical reactions in an organism?", "options": ["A.Metabolism", "B.Catabolism", "C.Anabolism", "D.Photosynthesis"], "answer": "A"},
    {"question": "45. What is the name of the process by which cells release energy from food molecules?", "options": ["A.Cellular Respiration", "B.Photosynthesis", "C.Fermentation", "D.Glycolysis"], "answer": "A"},
    {"question": "46. Which macromolecule is primarily responsible for genetic information storage and transfer?", "options": ["A.Nucleic Acids", "B.Proteins", "C.Carbohydrates", "D.Lipids"], "answer": "A"},
    {"question": "47. What is the name of the cellular process that results in the production of two identical daughter cells?", "options": ["A.Mitosis", "B.Meiosis", "C.Binary Fission", "D.Budding"], "answer": "A"},
    {"question": "48. What is the term for a segment of DNA that codes for a specific protein or function?", "options": ["A.Gene", "B.Chromosome", "C.Nucleotide", "D.Allele"], "answer": "A"},
    {"question": "49. What is the primary role of the lysosome?", "options": ["A.Digesting Cellular Waste", "B.Energy Production", "C.Protein Synthesis", "D.Cell Division"], "answer": "A"},
    {"question": "50. Which organelle is involved in producing ribosomes?", "options": ["A.Nucleolus", "B.Nucleus", "C.Mitochondria", "D.Endoplasmic Reticulum"], "answer": "A"}
    
] 
    for objectiv in biology_questions:
            print(objectiv["question"])
            for opt in objectiv["options"]:
                print(opt)
            answer = input("Choose an option between (A, B, C, and D): ").upper()
            if answer == objectiv["answer"]:
                
                global score
                score += 10
            else:
                
                score += 0
         
def General():

    General_questions = [
    
    
    {"question": "1. What is the capital of Australia?", "options": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"], "answer": "B"},
    {"question": "2. Who wrote 'To Kill a Mockingbird'?", "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Mark Twain", "D. Ernest Hemingway"], "answer": "A"},
    {"question": "3. What is the largest planet in our solar system?", "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": "C"},
    {"question": "4. What year did the Titanic sink?", "options": ["A. 1910", "B. 1912", "C. 1914", "D. 1916"], "answer": "B"},
    {"question": "5.What is the chemical symbol for gold?", "options": ["A. Au", "B. Ag", "C. Pb", "D. Fe"], "answer": "A"},
    {"question": "6. Who painted the Mona Lisa?", "options": ["A. Vincent Van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Claude Monet"], "answer": "B"},
    {"question": "7. What is the hardest natural substance on Earth?", "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Platinum"], "answer": "C"},
    {"question": "8. Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"], "answer": "B"},
    {"question": "9. What is the largest ocean on Earth?", "options": ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"], "answer": "B"},
    {"question": "10. Who was the first person to walk on the moon?", "options": ["A. Neil Armstrong", "B. Buzz Aldrin", "C. Yuri Gagarin", "D. Michael Collins"], "answer": "A"},
    {"question": "11. What is the capital of Canada?", "options": ["A. Toronto", "B. Ottawa", "C. Vancouver", "D. Montreal"], "answer": "B"},
    {"question": "12. What is the smallest country in the world?", "options": ["A. Monaco", "B. Liechtenstein", "C. Vatican City", "D. San Marino"], "answer": "C"},
    {"question": "13. Which element has the atomic number 1?", "options": ["A. Helium", "B. Hydrogen", "C. Lithium", "D. Beryllium"], "answer": "B"},
    {"question": "14. In which country is the Great Wall located?", "options": ["A. Japan", "B. India", "C. China", "D. Korea"], "answer": "C"},
    {"question": "15. Who is known as the 'Father of Computers'?", "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"], "answer": "A"},
    {"question": "16. Wh1at is the capital of France?", "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"], "answer": "A"},
    {"question": "17. What is the longest river in the world?", "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"], "answer": "A"},
    {"question": "18. Who wrote 'Pride and Prejudice'?", "options": ["A. Jane Austen", "B. Charlotte Brontë", "C. Emily Dickinson", "D. Louisa May Alcott"], "answer": "A"},
    {"question": "19. What is the name of the galaxy we live in?", "options": ["A. Andromeda", "B. Milky Way", "C. Triangulum", "D. Messier 87"], "answer": "B"},
    {"question": "20. Which ocean is the largest?", "options": ["A. Pacific", "B. Atlantic", "C. Indian", "D. Arctic"], "answer": "A"},
    {"question": "21. Which country is known as the Land of the Rising Sun?", "options": ["Japan", "China", "Thailand", "South Korea"], "answer": "Japan"},
    {"question": "22. Who was the first President of the United States?", "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "answer": "George Washington"},
    {"question": "23. Which continent is the Sahara Desert located in?", "options": ["Africa", "Asia", "Australia", "South America"], "answer": "Africa"},
    {"question": "24. In which year did the Titanic sink?", "options": ["1912", "1905", "1920", "1915"], "answer": "1912"},
    {"question": "25. What is the capital city of Canada?", "options": ["Ottawa", "Toronto", "Vancouver", "Montreal"], "answer": "Ottawa"},
    {"question": "26. Which famous scientist developed the theory of relativity?", "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "answer": "Albert Einstein"},
    {"question": "27. What is the largest ocean on Earth?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": "Pacific Ocean"},
    {"question": "28. Who wrote the play 'Romeo and Juliet'?", "options": ["William Shakespeare", "George Bernard Shaw", "Charles Dickens", "J.K. Rowling"], "answer": "William Shakespeare"},
    {"question": "29. Which organization is responsible for maintaining international peace and security?", "options": ["United Nations", "World Health Organization", "International Monetary Fund", "World Trade Organization"], "answer": "United Nations"},
    {"question": "30. What is the currency of Japan?", "options": ["Yen", "Won", "Euro", "Dollar"], "answer": "Yen"},
    {"question": "31. Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "32. Who was the leader of the Soviet Union during World War II?", "options": ["Joseph Stalin", "Leon Trotsky", "Vladimir Lenin", "Nikita Khrushchev"], "answer": "Joseph Stalin"},
    {"question": "33. What is the name of the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"question": "34. Which U.S. state is known as the Sunshine State?", "options": ["Florida", "California", "Texas", "Hawaii"], "answer": "Florida"},
    {"question": "35. What is the chemical symbol for gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"},
    {"question": "36. Which country is the smallest by land area?", "options": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"], "answer": "Vatican City"},
    {"question": "37. Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "answer": "Leonardo da Vinci"},
    {"question": "38. What is the capital of Australia?", "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"], "answer": "Canberra"},
    {"question": "39. Which country is known for the Great Wall?", "options": ["China", "India", "Japan", "South Korea"], "answer": "China"},
    {"question": "40. In which year did the Berlin Wall fall?", "options": ["1989", "1987", "1991", "1985"], "answer": "1989"},
    {"question": "41. Who is known as the Father of Modern Physics?", "options": ["Albert Einstein", "Isaac Newton", "James Clerk Maxwell", "Niels Bohr"], "answer": "Albert Einstein"},
    {"question": "42. What is the capital city of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "43. Which element has the atomic number 1?", "options": ["Hydrogen", "Helium", "Oxygen", "Nitrogen"], "answer": "Hydrogen"},
    {"question": "44. Which river is known as the 'Yellow River'?", "options": ["Huang He", "Yangtze", "Mekong", "Ganges"], "answer": "Huang He"},
    {"question": "45. Who was the first man to walk on the moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"], "answer": "Neil Armstrong"},
    {"question": "46. What is the capital of Brazil?", "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"], "answer": "Brasília"},
    {"question": "47. Which famous explorer is credited with discovering America in 1492?", "options": ["Christopher Columbus", "Ferdinand Magellan", "Vasco da Gama", "James Cook"], "answer": "Christopher Columbus"},
     {"question": "48. What is the largest desert in the world?", "options": ["Antarctic Desert", "Sahara Desert", "Arabian Desert", "Gobi Desert"], "answer": "Antarctic Desert"},
    {"question": "49. Which famous shipwreck occurred in 1912?", "options": ["Titanic", "Lusitania", "Bismarck", "Andrea Doria"], "answer": "Titanic"},
    {"question": "50. What is the most spoken language in the world?", "options": ["Mandarin Chinese", "English", "Spanish", "Hindi"], "answer": "Mandarin Chinese"}

    
    
]
    score = 0
    for objective in General_questions:
         print(objective["question"])
         for opt in objective["options"]:
             print(opt)
         answer = input("Choose an option between (A, B, C, and D): ").upper()
         if answer == objective["answer"]:
             
             score += 1
         else:
               score += 0
             
def English():
    english_questions = [
    {"question": "1. What is the synonym of 'happy'?", "options": ["A. Sad", "B. Joyful", "C. Angry", "D. Tired"], "answer": "B"},
    {"question": "2. Choose the correct sentence:", "options": ["A. She don't like apples.", "B. She doesn't likes apples.", "C. She don't likes apples.", "D. She doesn't like apples."], "answer": "D"},
    {"question": "3. What is the antonym of 'difficult'?", "options": ["A. Easy", "B. Hard", "C. Tough", "D. Complicated"], "answer": "A"},
    {"question": "4. Which of the following is a verb?", "options": ["A. Quickly", "B. Book", "C. Run", "D. Beautiful"], "answer": "C"},
    {"question": "5. Which word is a noun?", "options": ["A. Happiness", "B. Run", "C. Quickly", "D. Easily" ], "answer": "A"},
    {"question": "6. Identify the adverb in the sentence: 'She sings beautifully.'", "options": ["A. She", "B. Sings", "C. Beautifully", "D. None"], "answer": "C"},
    {"question": "7. What is the plural of 'mouse'?", "options": ["A. Mice", "B. Mouses", "C. Mouse", "D. Mices"], "answer": "A"},
    {"question": "8. What is the past tense of 'go'?", "options": ["A. Goes", "B. Went", "C. Gone", "D. Going"], "answer": "B"},
    {"question": "9. Which of the following sentences is correct?", "options": ["A. He don't have a pen.", "B. He doesn't have a pen.", "C. He doesn't has a pen.", "D. He don't has a pen."], "answer": "B"},
    {"question": "10 Which punctuation mark is used to show a question?", "options": ["A. Period", "B. Exclamation mark", "C. Comma", "D. Question mark"], "answer": "D"},
    {"question": "11. What is the antonym of 'difficult'?", "options": ["A.easy", "B.hard", "C.complicated", "D.complex"], "answer": "A"},
    {"question": "12. Which of the following is a proper noun?", "options": ["city", "dog", "John", "book"], "answer": "John"},
    {"question": "13.What is the past tense of 'run'?", "options": ["ran", "running", "runs", "runed"], "answer": "ran"},
    {"question": "14.Identify the sentence that is grammatically correct.", "options": ["She don't like apples.", "She doesn't likes apples.", "She doesn't like apples.", "She don't likes apples."], "answer": "She doesn't like apples."},
    {"question": "15. Which of the following sentences is in the passive voice?", "options": ["The cat chased the mouse.", "The mouse was chased by the cat.", "The cat chases the mouse.", "The mouse chases the cat."], "answer": "The mouse was chased by the cat."},
    {"question": "16. What is the plural form of 'child'?", "options": ["childs", "children", "childes", "childer"], "answer": "children"},
    {"question": "17. What is the correct spelling?", "options": ["definitely", "definately", "definitly", "definatly"], "answer": "definitely"},
    {"question": "18. Complete the idiom: 'Bite the ___.'", "options": ["bullet", "hand", "dust", "tongue"], "answer": "bullet"},
    {"question": "19. What is the synonym of 'quick'?", "options": ["fast", "slow", "steady", "delayed"], "answer": "fast"},
    {"question": "20. Which word means 'to make an effort to do something'?", "options": ["attempt", "neglect", "refuse", "ignore"], "answer": "attempt"},
    {"question": "21. Choose the correct sentence.", "options": ["They was going to the store.", "They were going to the store.", "They is going to the store.", "They be going to the store."], "answer": "They were going to the store."},
    {"question": "22. What is the antonym of 'arrive'?", "options": ["depart", "come", "reach", "enter"], "answer": "depart"},
    {"question": "23. What is the term for a word that has the same meaning as another word?", "options": ["Synonym", "Antonym", "Homonym", "Homophone"], "answer": "Synonym"},
    {"question": "24. Which sentence is correct?", "options": ["Its raining outside.", "It's raining outside.", "Its raining outside.", "Its rainning outside."], "answer": "It's raining outside."},
    {"question": "25. What is the main verb in the sentence: 'She quickly wrote the letter.'?", "options": ["wrote", "quickly", "letter", "She"], "answer": "wrote"},
    {"question": "26. Complete the sentence: 'If I ___ you, I would apologize.'", "options": ["was", "were", "am", "be"], "answer": "were"},
    {"question": "27. Choose the correct usage of 'their':", "options": ["Their going to the park.", "They're going to the park.", "There going to the park.", "Their going to the parks."], "answer": "They're going to the park."},
    {"question": "28. What does the word 'benevolent' mean?", "options": ["kind", "harsh", "selfish", "indifferent"], "answer": "kind"},
    {"question": "29. Which of the following sentences is a question?", "options": ["She went to the store.", "Did she go to the store?", "She goes to the store.", "She is going to the store."], "answer": "Did she go to the store?"},
    {"question": "30. What is the correct plural form of 'mouse'?", "options": ["mouses", "mice", "mouses", "mices"], "answer": "mice"},
    {"question": "31. What is the adjective in the sentence: 'The tall man walked quickly.'?", "options": ["tall", "man", "walked", "quickly"], "answer": "tall"},
    {"question": "32. Which of the following is a compound sentence?", "options": ["I went to the store, and I bought some bread.", "I went to the store. I bought some bread.", "I went to the store because I needed bread.", "Going to the store was fun."], "answer": "I went to the store, and I bought some bread."},
    {"question": "33. What is the past perfect tense of 'eat'?", "options": ["had eaten", "eaten", "ate", "eats"], "answer": "had eaten"},
    {"question": "34. Which sentence uses the word 'affect' correctly?", "options": ["The new policy will affect all employees.", "The new policy will effect all employees.", "The new policy will affect all employee's.", "The new policy will affect all employee."], "answer": "The new policy will affect all employees."},
    {"question": "35. What is the correct comparative form of 'good'?", "options": ["better", "gooder", "more good", "best"], "answer": "better"},
    {"question": "36. Choose the correctly punctuated sentence.", "options": ["I have a cat a dog, and a bird.", "I have a cat, a dog and a bird.", "I have a cat, a dog, and a bird.", "I have a cat, a dog and, a bird."], "answer": "I have a cat, a dog, and a bird."},
    {"question": "37. What is the meaning of the word 'euphoria'?", "options": ["extreme happiness", "extreme sadness", "anger", "fear"], "answer": "extreme happiness"},
    {"question": "38. Which of the following sentences contains a prepositional phrase?", "options": ["The book on the table is mine.", "I read the book.", "She runs quickly.", "The cat slept."], "answer": "The book on the table is mine."},
    {"question": "39. What is the adverb in the sentence: 'He spoke loudly during the meeting.'?", "options": ["spoke", "loudly", "meeting", "during"], "answer": "loudly"},
    {"question": "40. What is the correct verb form: 'She ___ to the gym every day.'", "options": ["go", "goes", "gone", "going"], "answer": "goes"},
    {"question": "41. Which sentence is in the future tense?", "options": ["She walks to school.", "She walked to school.", "She will walk to school.", "She is walking to school."], "answer": "She will walk to school."},
    {"question": "42. Choose the correct sentence.", "options": ["Their is a problem with the report.", "There is a problem with the report.", "They're is a problem with the report.", "There are a problem with the report."], "answer": "There is a problem with the report."},
    {"question": "43. What is the correct usage of 'who' and 'whom'?", "options": ["Who is coming to the party?", "Whom is coming to the party?", "Who is the book written by?", "Whom is the book written by?"], "answer": "Who is coming to the party?"},
    {"question": "44. Complete the sentence: 'I ___ finished my homework before dinner.'", "options": ["have", "had", "has", "having"], "answer": "had"},
    {"question": "45. Which of the following sentences is an example of a simile?", "options": ["She is as brave as a lion.", "She is brave.", "She is a lion.", "She is brave like a lion."], "answer": "She is as brave as a lion."},
    {"question": "46. What is the meaning of the word 'meticulous'?", "options": ["careful and precise", "lazy", "quick", "disorganized"], "answer": "careful and precise"},
    {"question": "47. What is the correct way to write the plural of 'party'?", "options": ["parties", "partys", "party's", "partys"], "answer": "parties"},
    {"question": "48. What is the proper use of 'your' and 'you're'?", "options": ["Your book is on the table.", "You're book is on the table.", "Your're book is on the table.", "Youre book is on the table."], "answer": "Your book is on the table."},
    {"question": "49. Which of the following is a simple sentence?", "options": ["She went to the store, and he stayed home.", "Although she went to the store, he stayed home.", "She went to the store.", "She went to the store because she needed milk."], "answer": "She went to the store."},
    
]
    
    for object in english_questions :
            print(object["question"])
            for opt in object["options"]:
                print(opt)
            answer = input("Choose an option between (A, B, C, and D): ").upper()
            if answer == object["answer"]:
                
                global score 
                score += 10
            else:
                
                score += 0 
    
def Mathematics():
    mathematics_questions = [
    {"question": "1. What is 7 + 5?", "options": ["A. 12", "B. 10", "C. 15", "D. 14"], "answer": "A"},
    {"question": "2. What is 9 - 4?", "options": ["A. 6", "B. 5", "C. 4", "D. 7"], "answer": "B"},
    {"question": "3. What is 6 x 8?", "options": ["A. 42", "B. 48", "C. 54", "D. 56"], "answer": "B"},
    {"question": "4. What is 81 / 9?", "options": ["A. 9", "B. 8", "C. 7", "D. 10"], "answer": "A"},
    {"question": "5. What is 5 squared?", "options": ["A. 20", "B. 25", "C. 30", "D. 35"], "answer": "B"},
    {"question": "6. What is the square root of 49?", "options": ["A. 6", "B. 7", "C. 8", "D. 9"], "answer": "B"},
    {"question": "7. What is the result of 15 % 4?", "options": ["A. 1", "B. 2", "C. 3", "D. 4"], "answer": "C"},
    {"question": "8. What is 25 + 17?", "options": ["A. 42", "B. 40", "C. 37", "D. 35"], "answer": "A"},
    {"question": "9. What is 12 x 12?", "options": ["A. 144", "B. 132", "C. 120", "D. 108"], "answer": "A"},
    {"question": "10. What is the value of π (pi) approximately?", "options": ["A. 3.14", "B. 3.16", "C. 3.20", "D. 3.10"], "answer": "A"},

    {"question": "11. What is 4 * 9?", "options": ["A. 38", "B. 36", "C. 28", "D. 40"], "answer": "B"},
    {"question": "12. What is 100 - 37?", "options": ["73", "67", "63", "77"], "answer": "C"},
    {"question": "13. What is 15^2?", "options": ["275", "200", "250", "225"], "answer": "D"},
    {"question": "14. Solve for x: 2x + 5 = 15", "options": ["15", "10", "7", "5"], "answer": "D"},
    {"question": "15. What is the value of 3 * (2 + 4)?", "options": ["18", "21", "24", "26"], "answer": "A"},
    {"question": "16. What is 20% of 150?", "options": ["30", "25", "20", "35"], "answer": "A"},
    {"question": "17. What is the next number in the sequence: 2, 4, 8, 16, ?", "options": ["22", "32", "18", "28"], "answer": "A"},
    {"question": "18. What is 7 + 3 * 2?", "options": ["10", "13", "20", "18"], "answer": "B"},
    {"question": "19. Find the area of a rectangle with length 8 cm and width 5 cm.", "options": ["80 cm^2", "30 cm^2", "40 cm^2", "45 cm^2"], "answer": "C"},
    {"question": "20. What is 9 squared?", "options": ["99", "72", "90", "81"], "answer": "D"},
    {"question": "21. What is the value of x in the equation 4x - 3 = 13?", "options": ["8", "4", "6", "7"], "answer": "B"},
    {"question": "22. What is the median of the following numbers: 3, 7, 5, 9, 12?", "options": ["5", "7", "6", "9"], "answer": "D"},
    {"question": "23. Find the perimeter of a triangle with sides 6 cm, 8 cm, and 10 cm.", "options": ["24 cm", "26 cm", "22 cm", "20 cm"], "answer": "A cm"},
    {"question": "24. What is the value of 5! (5 factorial)?", "options": ["130", "120", "60", "24"], "answer": "B"},
    {"question": "25. What is the square of 7?", "options": ["42", "56", "49", "64"], "answer": "C"},
    {"question": "26. Solve for y: 3y - 2 = 10", "options": ["10", "6", "4", "12"], "answer": "C"},
    {"question": "27. What is the circumference of a circle with radius 7 cm? (Use π ≈ 3.14)", "options": ["40.96 cm", "44.00 cm", "43.96 cm", "45.50 cm"], "answer": "C"},
    {"question": "28. What is the volume of a cube with side length 3 cm?", "options": ["29 cm^3", "30 cm^3", "24 cm^3", "27 cm^3"], "answer": "D"},
    {"question": "29. What is the result of 50 divided by 5?", "options": ["15", "10", "8", "15"], "answer": "B"},
    {"question": "30. What is the area of a circle with diameter 10 cm? (Use π ≈ 3.14)", "options": ["76.5 cm^2", "78.5 cm^2", "100 cm^2", "31.4 cm^2"], "answer": "B"},
    {"question": "31. What is 3/4 + 1/4?", "options": ["1", "1/2", "2/4", "3/4"], "answer": "A"},
    {"question": "32. What is the hypotenuse of a right triangle with legs of length 6 cm and 8 cm?", "options": ["14 cm", "10 cm", "8 cm", "14 cm"], "answer": "B"},
    {"question": "33. What is the value of 2^5?", "options": ["36", "16", "32", "25"], "answer": "C"},
    {"question": "34. If the sum of two numbers is 30 and one of them is 12, what is the other number?", "options": ["18", "12", "20", "15"], "answer": "A"},
    {"question": "35. What is the largest prime number less than 20?", "options": ["17", "13", "19", "11"], "answer": "C"},
    {"question": "36. Solve for x: x/5 = 9", "options": ["40", "50", "45", "55"], "answer": "C"},
    {"question": "37. What is 8 + (2 * 5)?", "options": ["16", "20", "18", "22"], "answer": "C"},
    {"question": "38. What is the sum of the interior angles of a triangle?", "options": ["270 degrees", "90 degrees", "360 degrees", "180 degrees"], "answer": "D"},
    {"question": "39. What is the value of √81?", "options": ["9", "8", "10", "7"], "answer": "A"},
    {"question": "40. Find the average of these numbers: 4, 8, 12, 16.", "options": ["14", "12", "10", "8"], "answer": "C"},
    {"question": "41. What is 14 - 7 + 3?", "options": ["11", "12", "9", "10"], "answer": "D"},
    {"question": "42. What is the value of 7 * (4 - 2)?", "options": ["15", "12", "16", "14"], "answer": "D"},
    {"question": "43. Solve for z: 2z + 6 = 18", "options": ["5", "6", "7", "8"], "answer": "B"},
    {"question": "44. What is 25% of 80?", "options": ["24", "25", "15", "20"], "answer": "D"},
    {"question": "45. What is the surface area of a cube with side length 4 cm?", "options": ["86 cm^2", "64 cm^2", "80 cm^2", "96 cm^2"], "answer": "D"},
    {"question": "46. What is the result of 7^3?", "options": ["353", "343", "300", "336"], "answer": "B"},
    {"question": "47. What is the difference between the highest and lowest number in this set: 12, 23, 7, 19?", "options": ["20", "15", "14", "16"], "answer": "D"},
    {"question": "48. What is 3/5 - 1/10?", "options": ["3/2", "1/5", "3/10", "1/2"], "answer": "D"},
    {"question": "49. Find the median of these numbers: 9, 1, 6, 4, 7", "options": ["9", "7", "5", "6"], "answer": "D"},
    {"question": "50. What is 6 * 6 / 3?", "options": ["12", "18", "15", "10"], "answer": "A"}


]   
    for objective in mathematics_questions:
                print(objective["question"])
                for opt in objective["options"]:
                    print(opt)
                answer = input("Choose an option between (A, B, C, and D): ").upper()
                if answer == objective["answer"]:
                    
                    global score 
                    score += 10 
                
                else: 
                    
                    score = 0
    