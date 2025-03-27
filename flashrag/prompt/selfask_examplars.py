SELF_ASK_PROMPT_SINGLE_HOP = """Given the following question, answer it by providing follow up questions and intermediate answers. If intermediate questions are not necessarry, answer the question directly. You are provided with evidence that can help you arrive at the answer before the question.
#
Context1: The Big Red One: Fuller was a World War II veteran and served with the 1st Infantry Division, which is nicknamed "The Big Red One" for the red numeral "1" on the division's shoulder patch. He received the Silver Star, Bronze Star, and Purple Heart during his service.
Question: how did the big red one get its name
Are follow up questions needed here: No.
So the final answer is: its shoulder patch
#
Context1: Module:Location map/data/Cayman Islands: Module:Location map/data/Cayman Islands is a location map definition used to overlay markers and labels on an equirectangular projection map of Cayman
Question: where are the cayman islands on the map
Are follow up questions needed here: No.
So the final answer is: western Caribbean Sea
#
Context1: Korean War | Combatants, Summary, Years, Map ... - Britannica: After more than a million combat casualties had been suffered on both sides, the fighting ended in July 1953 with Korea still divided into two hostile states. Negotiations in 1954 produced no further agreement, and the front line has been accepted ever since as the de facto boundary between North and South Korea.
Question: who won the war between north korea and south korea
Are follow up questions needed here: No.
So the final answer is: technically still at war
#
Context1: It's Always Sunny in Philadelphia (season 13): The thirteenth season of the American comedy television series It's Always Sunny in Philadelphia premiered on FXX on September 5, 2018.
Question: when does it's always sunny in philadelphia season 13 start
Are follow up questions needed here: No.
So the final answer is: September 5, 2018
#
Context1: You've Got a Friend in Me: "You've Got a Friend in Me" is a song by Randy Newman. Used as the theme song for the 1995 Disney/Pixar animated film Toy Story, it has since become a major ...
Question: who sang you got a friend in me from toy story
Are follow up questions needed here: No.
So the final answer is: Randy Newman
#
Context1: Timeline of space exploration: This is a timeline of space exploration which includes notable achievements, first accomplishments and milestones in humanity's exploration of outer space.
Question: when was the first person sent to space
Are follow up questions needed here: No.
So the final answer is: 12 April 1961
#"""


SELF_ASK_PROMPT_MULTI_HOP = """Given the following question, answer it by providing follow up questions and intermediate answers. If intermediate questions are not necessarry, answer the question directly. You are provided with evidence that can help you arrive at the answer before the question.
#
Context1: Xawery Żuławski: Polish-Russian War (Wojna polsko-ruska) is a 2009 Polish film directed by Xawery Żuławski based on the novel Polish-Russian War under the white-red flag by Dorota Masłowska. So the answer is Xawery Żuławski.
Context2: Xawery Żuławski: Xawery Żuławski ; National Film School in Łódź · 1995–present · Maria Strzelecka · 2.
Question: Who is the mother of the director of film Polish-Russian War (Film)?
Are follow up questions needed here: Yes.
Follow up: Who is the director of the film Polish-Russian War (Film)?
Intermediate answer: The director of the film Polish-Russian War is Xawery Żuławski.
Follow up: Who is the mother of Xawery Żuławski?
Intermediate answer: The mother of Xawery Żuławski is Małgorzata Braunek.
So the final answer is: Rick Scott Małgorzata Braunek.
#
Context1: 2003: Blind Shaft (Chinese: 盲井; pinyin: Mángjǐng) is a 2003 film about a pair of brutal con artists operating in the illegal coal mines of present-day northern China. So the answer is 2003.
Context2: December 2, 1932: Release and reception. The Mask of Fu Manchu opened in New York on December 2, 1932. The film cost a total of $338,000 and had worldwide rentals of $625,000. It had a profit of $62,000. So the answer is December 2, 1932.
Question: Which film came out first, Blind Shaft or The Mask Of Fu Manchu?
Are follow up questions needed here: Yes.
Follow up: When did Blind Shaft come out?
Intermediate answer: Blind Shaft came out in 2003.
Follow up: When did The Mask Of Fu Manchu come out?
Intermediate answer: The Mask Of Fu Manchu came out in 1932.
So the final answer is: The Mask Of Fu Manchu.
#
Context1: John V, Prince of Anhalt-Zerbst: John was the second (but eldest surviving) son of Ernest I, Prince of Anhalt-Dessau, by his wife Margarete, daughter of Henry I, Duke of Münsterberg-Oels, and granddaughter of George of Poděbrady, King of Bohemia.
Context2: 12 June 1516: Ernest I, Prince of Anhalt-Dessau (died Dessau, 12 June 1516), was a German prince of the House of Ascania and ruler of the principality of Anhalt-Dessau. So the answer is 12 June 1516.
Question: When did John V, Prince Of Anhalt-Zerbst's father die?
Are follow up questions needed here: Yes.
Follow up: Who is the father of John V, Prince Of Anhalt-Zerbst?
Intermediate answer: The father of John V, Prince Of Anhalt-Zerbst is Ernest I, Prince of Anhalt-Dessau.
Follow up: When did Ernest I, Prince of Anhalt-Dessau die?
Intermediate answer: Ernest I, Prince of Anhalt-Dessau died on 12 June 1516.
So the final answer is: 12 June 1516
#
Context1: El extraño viaje: El extraño viaje (English: The Strange Voyage) is a 1964 Spanish black drama film directed by Fernando Fernán Gómez.
Context2: Love in Pawn: Love in Pawn is a 1953 British comedy film directed by Charles Saunders and starring Bernard Braden, Barbara Kelly and Jeannie Carson.
Context3: 28 August 1921: Fernando Fernández Gómez (28 August 1921 – 21 November 2007) better known as Fernando Fernán Gómez was a Spanish actor, screenwriter, film director, theater director and member of the Royal Spanish Academy for seven years. So the answer is 28 August 1921.
Context4: Charles Saunders (director): Charles Joel Saunders (8 April 1904 – 20 April 1997) was an English film director and screenwriter who began in the industry as a film editor, and who also contributed to television.
Question: Which film has the director who was born later, El Extraño Viaje or Love In Pawn?
Are follow up questions needed here: Yes.
Follow up: Who is the director of El Extraño Viaje?
Intermediate answer: The director of El Extraño Viaje is Fernando Fernán Gómez.
Follow up: Who is the director of Love in Pawn?
Intermediate answer: The director of Love in Pawn is Charles Saunders.
Follow up: When was Fernando Fernán Gómez born?
Intermediate answer: Fernando Fernán Gómez was born on 28 August 1921.
Follow up: When was Charles Saunders (director) born?
Intermediate answer: Charles Saunders was born on 8 April 1904.
So the final answer is: El Extraño Viaje.
#
Context1: John, Count Palatine of Neumarkt: John (Johann von Pfalz-Neumarkt; 1383 – 14 March 1443) was the Count Palatine of Neumarkt from 1410 to his death. The son of Rupert III of the Palatinate, he married Catherine of Pomerania in 1407.
Context2: John, Count Palatine of Neumarkt: John (Johann von Pfalz-Neumarkt; 1383 – 14 March 1443) was the Count Palatine of Neumarkt from 1410 to his death. The son of Rupert III of the Palatinate, he married Catherine of Pomerania in 1407.
Question: Who is Catherine Of Pomerania, Countess Palatine Of Neumarkt's father-in-law?
Are follow up questions needed here: Yes.
Follow up: Who is the husband of Catherine of Pomerania, Countess Palatine of Neumarkt?
Intermediate answer: The husband of Catherine of Pomerania, Countess Palatine of Neumarkt is John, Count Palatine of Neumarkt.
Follow up: Who is the father of John, Count Palatine of Neumarkt?
Intermediate answer: The father of John, Count Palatine of Neumarkt is Rupert III of the Palatinate.
So the final answer is: Rupert III of the Palatinate.
#
Context1: Crimen a las tres: Crimen a las tres is a 1935 Argentine crime film directed and written by Luis Saslavsky. Crimen a las tres. Directed by, Luis Saslavsky.
Context2: Elio Petri: The Working Class Goes to Heaven (Italian: La classe operaia va in paradiso), released in the US as Lulu the Tool, is a 1971 political drama film directed by Elio Petri. So the answer is Elio Petri.
Context3: March 20, 1995: Luis Saslavsky (April 21, 1903 – March 20, 1995) was an Argentine film director, screenwriter and film producer, and one of the influential directors in the Cinema of Argentina of the classic era. So the answer is March 20, 1995.
Context4: Elio Petri: Final years. In 1981, Petri visited Geneva to direct Arthur Miller\'s new play The American Clock, with Marcello Mastroianni playing the lead role. Petri died of cancer on 10 November 1982. He was 53 years old.
Question: Which film has the director died first, Crimen A Las Tres or The Working Class Goes To Heaven?
Are follow up questions needed here: Yes.
Follow up: Who is the director of Crimen a las tres?
Intermediate answer: The director of Crimen a las tres is Luis Saslavsky.
Follow up: Who is the director of The Working Class Goes to Heaven?
Intermediate answer: The director of The Working Class Goes to Heaven is Elio Petri.
Follow up: When did Luis Saslavsky die?
Intermediate answer: Luis Saslavsky died on March 20, 1995.
Follow up: When did Elio Petri die?
Intermediate answer: Elio Petri died on 10 November 1982.
So the final answer is: The Working Class Goes to Heaven
#"""

SELF_ASK_PROMPT_MULTI_HOP_PW = """Given the following question, answer it by providing follow up questions and intermediate answers. If intermediate questions are not necessarry, answer the question directly. You are provided with evidence that can help you arrive at the answer before the question.
#
Context1: # Aida Wang ## Family The sisters of Aida Wang are Barabara Beltran, Vicki Hackworth.  The mother of Aida Wang is Shelli Beltran.  The father of Aida Wang is Dino Beltran.  The daughter of Aida Wang is Johnetta Wang.  The husband of Aida Wang is Ryan Wang.  ## Friends The friends of Aida Wang are Alvaro Smock, Lannie Smock, Leslee Toombs, Ryan Wang.  ## Attributes The date of birth of Aida Wang is 0985-05-30.  The occupation of Aida Wang is personal assistant.  The hobby of Aida Wang is meditation.  The gender of Aida Wang is female.
Question: Who is the sister of Aida Wang?
Are follow up questions needed here: Yes.
Follow up: Who is the sister of Aida Wang?
Intermediate answer: The sisters of Aida Wang are Barabara Beltran, Vicki Hackworth. So the answer is Barabara Beltran, Vicki Hackworth.
So the final answer is: Barabara Beltran, Vicki Hackworth
#
Context1: # Alvaro Smock ## Family The sons of Alvaro Smock are Eli Smock, Gene Smock.  The wife of Alvaro Smock is Lannie Smock.  ## Friends The friends of Alvaro Smock are Dino Beltran, Gene Smock, Aida Wang.  ## Attributes The date of birth of Alvaro Smock is 0867-07-12.  The occupation of Alvaro Smock is osteopath.  The hobby of Alvaro Smock is biology
Question: Who is the child of Alvaro Smock?
Are follow up questions needed here: Yes.
Follow up: Who is the child of Alvaro Smock?
Intermediate answer: The children of Alvaro Smock are Eli Smock, Gene Smock. So the answer is Eli Smock, Gene Smock.
So the final answer is: Eli Smock, Gene Smock
#
Context1: # Alvaro Smock ## Family The sons of Alvaro Smock are Eli Smock, Gene Smock.  The wife of Alvaro Smock is Lannie Smock.  ## Friends The friends of Alvaro Smock are Dino Beltran, Gene Smock, Aida Wang.  ## Attributes The date of birth of Alvaro Smock is 0867-07-12.  The occupation of Alvaro Smock is osteopath.  The hobby of Alvaro Smock is biology.  The gender of Alvaro Smock is male.
Context2: # Eli Smock ## Family The brother of Eli Smock is Gene Smock.  The mother of Eli Smock is Lannie Smock.  The father of Eli Smock is Alvaro Smock.  ## Friends The friends of Eli Smock are Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran.  ## Attributes The date of birth of Eli Smock is 0901-01-18.  The occupation of Eli Smock is retail manager.  The hobby of Eli Smock is tether car.  The gender of Eli Smock is male.
Context3: # Gene Smock ## Family The brother of Gene Smock is Eli Smock.  The mother of Gene Smock is Lannie Smock.  The father of Gene Smock is Alvaro Smock.  The son of Gene Smock is Williams Smock.  The wife of Gene Smock is Dominique Smock.  ## Friends The friends of Gene Smock are Leeann Hackworth, Leisa Lutz, Ricardo Hackworth, Alvaro Smock, Dominique Smock.  ## Attributes The date of birth of Gene Smock is 0898-08-16.  The occupation of Gene Smock is immunologist.  The hobby of Gene Smock is architecture.  The gender of Gene Smock is male.
Question: Who is the friend of the child of Alvaro Smock?
Are follow up questions needed here: Yes.
Follow up: Who is the child of Alvaro Smock?
Intermediate answer: The children of Alvaro Smock are Eli Smock, Gene Smock.
Follow up: Who is the friend of Eli Smock and Gene Smock?
Intermediate answer: The friends of Eli Smock are Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran. The friends of Gene Smock are Leeann Hackworth, Leisa Lutz, Ricardo Hackworth, Alvaro Smock, Dominique Smock.
So the final answer is: Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran, Leeann Hackworth, Ricardo Hackworth, Dominique Smock
#
Context1: # Vicki Hackworth ## Family The sisters of Vicki Hackworth are Aida Wang, Barabara Beltran.  The mother of Vicki Hackworth is Shelli Beltran.  The father of Vicki Hackworth is Dino Beltran.  The son of Vicki Hackworth is Virgil Hackworth.  The daughters of Vicki Hackworth are Leeann Hackworth, Leisa Lutz.  The husband of Vicki Hackworth is Ricardo Hackworth.  ## Friends The friends of Vicki Hackworth are Brian Beltran, Dominique Smock, Eli Smock.  ## Attributes The date of birth of Vicki Hackworth is 0985-05-30.  The occupation of Vicki Hackworth is police officer.  The hobby of Vicki Hackworth is meditation.  The gender of Vicki Hackworth is female.
Context2: # Shelli Beltran ## Family The sister of Shelli Beltran is Stacia Toombs.  The mother of Shelli Beltran is Alison Smock.  The father of Shelli Beltran is Williams Smock.  The daughters of Shelli Beltran are Aida Wang, Barabara Beltran, Vicki Hackworth.  The husband of Shelli Beltran is Dino Beltran.  ## Friends The friends of Shelli Beltran are Brian Beltran, Eli Smock, Isiah Lutz, Leslee Toombs, Lesley Lutz, Ryan Wang.  ## Attributes The date of birth of Shelli Beltran is 0958-03-08.  The occupation of Shelli Beltran is occupational therapist.  The hobby of Shelli Beltran is sociology.  The gender of Shelli Beltran is female.
Context3: # Dino Beltran ## Family The brother of Dino Beltran is Orlando Beltran.  The mother of Dino Beltran is Daisy Beltran.  The father of Dino Beltran is Brian Beltran.  The daughters of Dino Beltran are Aida Wang, Barabara Beltran, Vicki Hackworth.  The wife of Dino Beltran is Shelli Beltran.  ## Friends The friend of Dino Beltran is Alvaro Smock.  ## Attributes The date of birth of Dino Beltran is 0958-08-09.  The occupation of Dino Beltran is associate professor.  The hobby of Dino Beltran is shogi.  The gender of Dino Beltran is male.
Question: Who is the aunt of Vicki Hackworth?
Are follow up questions needed here: Yes.
Follow up: Who are the parents of Vicki Hackworth?
Intermediate answer: The mother of Vicki Hackworth is Shelli Beltran. The father of Vicki Hackworth is Dino Beltran.
Follow up: Who is the sister of Shelli Beltran and Dino Beltran? 
Intermediate answer: The sister of Shelli Beltran is Stacia Toombs. Dino Beltran has no sister.
So the final answer is: Stacia Toombs
#
Context1: # Stacia Toombs ## Family The sister of Stacia Toombs is Shelli Beltran.  The mother of Stacia Toombs is Alison Smock.  The father of Stacia Toombs is Williams Smock.  The daughter of Stacia Toombs is Leslee Toombs.  The husband of Stacia Toombs is Wilbert Toombs.  ## Friends The friends of Stacia Toombs are Brian Beltran, Isiah Lutz, Leeann Hackworth, Lesley Lutz, Ryan Wang.  ## Attributes The date of birth of Stacia Toombs is 0959-03-22.  The occupation of Stacia Toombs is actuary.  The hobby of Stacia Toombs is finance.  The gender of Stacia Toombs is female.
Context2: # Wilbert Toombs ## Family The daughter of Wilbert Toombs is Leslee Toombs.  The wife of Wilbert Toombs is Stacia Toombs.  ## Friends ## Attributes The date of birth of Wilbert Toombs is 0956-07-26.  The occupation of Wilbert Toombs is theatre manager.  The hobby of Wilbert Toombs is radio-controlled car racing.  The gender of Wilbert Toombs is male.
Question: What is the occupation of the husband of Stacia Toombs?
Are follow up questions needed here: Yes.
Follow up: Who is the husband of Stacia Toombs?
Intermediate answer: The husband of Stacia Toombs is Wilbert Toombs.
Follow up: What is the occupation of Wilbert Toombs?
Intermediate answer: The occupation of Wilbert Toombs is theatre manager.
So the final answer is: theatre manager
#
Context1: # Lannie Smock ## Family The sons of Lannie Smock are Eli Smock, Gene Smock.  The husband of Lannie Smock is Alvaro Smock.  ## Friends The friends of Lannie Smock are Williams Smock, Aida Wang, Alison Smock.  ## Attributes The date of birth of Lannie Smock is 0867-08-24.  The occupation of Lannie Smock is biomedical scientist.  The hobby of Lannie Smock is bus spotting.  The gender of Lannie Smock is female.
Context2: # Eli Smock ## Family The brother of Eli Smock is Gene Smock.  The mother of Eli Smock is Lannie Smock.  The father of Eli Smock is Alvaro Smock.  ## Friends The friends of Eli Smock are Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran.  ## Attributes The date of birth of Eli Smock is 0901-01-18.  The occupation of Eli Smock is retail manager.  The hobby of Eli Smock is tether car.  The gender of Eli Smock is male.
Context3: # Gene Smock ## Family The brother of Gene Smock is Eli Smock.  The mother of Gene Smock is Lannie Smock.  The father of Gene Smock is Alvaro Smock.  The son of Gene Smock is Williams Smock.  The wife of Gene Smock is Dominique Smock.  ## Friends The friends of Gene Smock are Leeann Hackworth, Leisa Lutz, Ricardo Hackworth, Alvaro Smock, Dominique Smock.  ## Attributes The date of birth of Gene Smock is 0898-08-16.  The occupation of Gene Smock is immunologist.  The hobby of Gene Smock is architecture.  The gender of Gene Smock is male.
Context4: # Dominique Smock ## Family The son of Dominique Smock is Williams Smock.  The husband of Dominique Smock is Gene Smock.  ## Friends The friends of Dominique Smock are Gene Smock, Isiah Lutz, Orlando Beltran, Vicki Hackworth.  ## Attributes The date of birth of Dominique Smock is 0897-09-08.  The occupation of Dominique Smock is sports therapist.  The hobby of Dominique Smock is dominoes.  The gender of Dominique Smock is female.
Question: What is the hobby of the daughter-in-law of Lannie Smock?
Are follow up questions needed here: Yes.
Follow up: Who is the son of Lannie Smock?
Intermediate answer: The sons of Lannie Smock are Eli Smock, Gene Smock.
Follow up: Who is the wife of Eli Smock and Gene Smock?
Intermediate answer: The wife of Eli Smock is not provided. The wife of Gene Smock is Dominique Smock. 
Follow up: What is the hobby of Dominique Smock?
Intermediate answer: The hobby of Dominique Smock is dominoes.
So the final answer is: dominoes
#

Context1: Stacia Toombs ## Family The sister of Stacia Toombs is Shelli Beltran.  The mother of Stacia Toombs is Alison Smock.  The father of Stacia Toombs is Williams Smock.  The daughter of Stacia Toombs is Leslee Toombs.  The husband of Stacia Toombs is Wilbert Toombs.  ## Friends The friends of Stacia Toombs are Brian Beltran, Isiah Lutz, Leeann Hackworth, Lesley Lutz, Ryan Wang.  ## Attributes The date of birth of Stacia Toombs is 0959-03-22.  The occupation of Stacia Toombs is actuary.  The hobby of Stacia Toombs is finance.  The gender of Stacia Toombs is female.
Question: What is the date of birth of the person whose hobby is finance?
Are follow up questions needed here: Yes.
Follow up: Who is the person whose hobby is finance?
Intermediate answer: The person whose hobby is finance is Stacia Toombs.
Follow up: What is the date of birth of Stacia Toombs?
Intermediate answer: The date of birth of Stacia Toombs is 0959-03-22.
So the final answer is: 0959-03-22
#
Context1: # Lannie Smock ## Family The sons of Lannie Smock are Eli Smock, Gene Smock.  The husband of Lannie Smock is Alvaro Smock.  ## Friends The friends of Lannie Smock are Williams Smock, Aida Wang, Alison Smock.  ## Attributes The date of birth of Lannie Smock is 0867-08-24.  The occupation of Lannie Smock is biomedical scientist.  The hobby of Lannie Smock is bus spotting.  The gender of Lannie Smock is female.
Context2: # Eli Smock ## Family The brother of Eli Smock is Gene Smock.  The mother of Eli Smock is Lannie Smock.  The father of Eli Smock is Alvaro Smock.  ## Friends The friends of Eli Smock are Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran.  ## Attributes The date of birth of Eli Smock is 0901-01-18.  The occupation of Eli Smock is retail manager.  The hobby of Eli Smock is tether car.  The gender of Eli Smock is male.
Context3: # Gene Smock ## Family The brother of Gene Smock is Eli Smock.  The mother of Gene Smock is Lannie Smock.  The father of Gene Smock is Alvaro Smock.  The son of Gene Smock is Williams Smock.  The wife of Gene Smock is Dominique Smock.  ## Friends The friends of Gene Smock are Leeann Hackworth, Leisa Lutz, Ricardo Hackworth, Alvaro Smock, Dominique Smock.  ## Attributes The date of birth of Gene Smock is 0898-08-16.  The occupation of Gene Smock is immunologist.  The hobby of Gene Smock is architecture.  The gender of Gene Smock is male.
Context4: # Williams Smock ## Family The mother of Williams Smock is Dominique Smock.  The father of Williams Smock is Gene Smock.  The daughters of Williams Smock are Shelli Beltran, Stacia Toombs.  The wife of Williams Smock is Alison Smock.  ## Friends The friend of Williams Smock is Lannie Smock.  ## Attributes The date of birth of Williams Smock is 0926-04-04.  The occupation of Williams Smock is clinical biochemist.  The hobby of Williams Smock is social studies.  The gender of Williams Smock is male.
Question: Who is the great-granddaughter of the person whose occupation is biomedical scientist?
Are follow up questions needed here: Yes.
Follow up: Who is the person whose occupation is biomedical scientist?
Intermediate answer: The person whose occupation is biomedical scientist is Lannie Smock.
Follow up: Who is the child of Lannie Smock?
Intermediate answer: The sons of Lannie Smock are Eli Smock, Gene Smock.
Follow up: Who is the child of Eli Smock and Gene Smock?
Intermediate answer: The son of Gene Smock is Williams Smock. The son of Eli Smock is not provided.
Follow up: Who is the daughter of Williams Smock?
Intermediate answer: The daughters of Williams Smock are Shelli Beltran, Stacia Toombs.
So the final answer is: Shelli Beltran, Stacia Toombs
#
Context1: # Ryan Wang ## Family The daughter of Ryan Wang is Johnetta Wang.  The wife of Ryan Wang is Aida Wang.  ## Friends The friends of Ryan Wang are Shelli Beltran, Stacia Toombs, Virgil Hackworth, Aida Wang.  ## Attributes The date of birth of Ryan Wang is 0982-03-17.  The occupation of Ryan Wang is chief of staff.  The hobby of Ryan Wang is fossil hunting.  The gender of Ryan Wang is male.
Question: How many friends does Ryan Wang have?
Are follow up questions needed here: Yes.
Follow up: Who is the friend of Ryan Wang?
Intermediate answer: The friends of Ryan Wang are Shelli Beltran, Stacia Toombs, Virgil Hackworth, Aida Wang.
So the final answer is: 4
#
Context1: # Alvaro Smock ## Family The sons of Alvaro Smock are Eli Smock, Gene Smock.  The wife of Alvaro Smock is Lannie Smock.  ## Friends The friends of Alvaro Smock are Dino Beltran, Gene Smock, Aida Wang.  ## Attributes The date of birth of Alvaro Smock is 0867-07-12.  The occupation of Alvaro Smock is osteopath.  The hobby of Alvaro Smock is biology.  The gender of Alvaro Smock is male.
Context2: # Eli Smock ## Family The brother of Eli Smock is Gene Smock.  The mother of Eli Smock is Lannie Smock.  The father of Eli Smock is Alvaro Smock.  ## Friends The friends of Eli Smock are Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran.  ## Attributes The date of birth of Eli Smock is 0901-01-18.  The occupation of Eli Smock is retail manager.  The hobby of Eli Smock is tether car.  The gender of Eli Smock is male.
Context3: # Gene Smock ## Family The brother of Gene Smock is Eli Smock.  The mother of Gene Smock is Lannie Smock.  The father of Gene Smock is Alvaro Smock.  The son of Gene Smock is Williams Smock.  The wife of Gene Smock is Dominique Smock.  ## Friends The friends of Gene Smock are Leeann Hackworth, Leisa Lutz, Ricardo Hackworth, Alvaro Smock, Dominique Smock.  ## Attributes The date of birth of Gene Smock is 0898-08-16.  The occupation of Gene Smock is immunologist.  The hobby of Gene Smock is architecture.  The gender of Gene Smock is male.
Question: How many friends does the child of Alvaro Smock have?
Are follow up questions needed here: Yes.
Follow up: Who is the child of Alvaro Smock?
Intermediate answer: The children of Alvaro Smock are Eli Smock, Gene Smock.
Follow up: Who are the friends of Eli Smock and Gene Smock?
Intermediate answer: The friends of Eli Smock are Leisa Lutz, Shelli Beltran, Vicki Hackworth, Virgil Hackworth, Alison Smock, Brian Beltran. The friends of Gene Smock are Leeann Hackworth, Leisa Lutz, Ricardo Hackworth, Alvaro Smock, Dominique Smock.
So the final answer is: 6,5
#
Context1: # Stacia Toombs ## Family The sister of Stacia Toombs is Shelli Beltran.  The mother of Stacia Toombs is Alison Smock.  The father of Stacia Toombs is Williams Smock.  The daughter of Stacia Toombs is Leslee Toombs.  The husband of Stacia Toombs is Wilbert Toombs.  ## Friends The friends of Stacia Toombs are Brian Beltran, Isiah Lutz, Leeann Hackworth, Lesley Lutz, Ryan Wang.  ## Attributes The date of birth of Stacia Toombs is 0959-03-22.  The occupation of Stacia Toombs is actuary.  The hobby of Stacia Toombs is finance.  The gender of Stacia Toombs is female.
Context2: # Brian Beltran ## Family The sons of Brian Beltran are Dino Beltran, Orlando Beltran.  The wife of Brian Beltran is Daisy Beltran.  ## Friends The friends of Brian Beltran are Eli Smock, Leeann Hackworth, Shelli Beltran, Stacia Toombs, Vicki Hackworth.  ## Attributes The date of birth of Brian Beltran is 0927-07-27.  The occupation of Brian Beltran is oncologist.  The hobby of Brian Beltran is dolls.  The gender of Brian Beltran is male.
Context3: # Isiah Lutz ## Family The son of Isiah Lutz is Lesley Lutz.  The wife of Isiah Lutz is Leisa Lutz.  ## Friends The friends of Isiah Lutz are Johnetta Wang, Ricardo Hackworth, Shelli Beltran, Stacia Toombs, Dominique Smock.  ## Attributes The date of birth of Isiah Lutz is 1014-10-18.  The occupation of Isiah Lutz is education administrator.  The hobby of Isiah Lutz is geocaching.  The gender of Isiah Lutz is male.
Context4: # Leeann Hackworth ## Family The sister of Leeann Hackworth is Leisa Lutz.  The brother of Leeann Hackworth is Virgil Hackworth.  The mother of Leeann Hackworth is Vicki Hackworth.  The father of Leeann Hackworth is Ricardo Hackworth.  ## Friends The friends of Leeann Hackworth are Stacia Toombs, Brian Beltran, Gene Smock.  ## Attributes The date of birth of Leeann Hackworth is 1011-10-25.  The occupation of Leeann Hackworth is music tutor.  The hobby of Leeann Hackworth is research.  The gender of Leeann Hackworth is female.
Context5: # Vicki Hackworth ## Family The sisters of Vicki Hackworth are Aida Wang, Barabara Beltran.  The mother of Vicki Hackworth is Shelli Beltran.  The father of Vicki Hackworth is Dino Beltran.  The son of Vicki Hackworth is Virgil Hackworth.  The daughters of Vicki Hackworth are Leeann Hackworth, Leisa Lutz.  The husband of Vicki Hackworth is Ricardo Hackworth.  ## Friends The friends of Vicki Hackworth are Brian Beltran, Dominique Smock, Eli Smock.  ## Attributes The date of birth of Vicki Hackworth is 0985-05-30.  The occupation of Vicki Hackworth is police officer.  The hobby of Vicki Hackworth is meditation.  The gender of Vicki Hackworth is female.
Context6: # Ricardo Hackworth ## Family The son of Ricardo Hackworth is Virgil Hackworth.  The daughters of Ricardo Hackworth are Leeann Hackworth, Leisa Lutz.  The wife of Ricardo Hackworth is Vicki Hackworth.  ## Friends The friends of Ricardo Hackworth are Gene Smock, Isiah Lutz, Johnetta Wang.  ## Attributes The date of birth of Ricardo Hackworth is 0983-02-24.  The occupation of Ricardo Hackworth is clinical research associate.  The hobby of Ricardo Hackworth is dairy farming.  The gender of Ricardo Hackworth is male.
Context7: # Lesley Lutz ## Family The mother of Lesley Lutz is Leisa Lutz.  The father of Lesley Lutz is Isiah Lutz.  ## Friends The friends of Lesley Lutz are Shelli Beltran, Stacia Toombs.  ## Attributes The date of birth of Lesley Lutz is 1040-01-31.  The occupation of Lesley Lutz is barrister's clerk.  The hobby of Lesley Lutz is canoeing.  The gender of Lesley Lutz is male.
Context8: # Leisa Lutz ## Family The sister of Leisa Lutz is Leeann Hackworth.  The brother of Leisa Lutz is Virgil Hackworth.  The mother of Leisa Lutz is Vicki Hackworth.  The father of Leisa Lutz is Ricardo Hackworth.  The son of Leisa Lutz is Lesley Lutz.  The husband of Leisa Lutz is Isiah Lutz.  ## Friends The friends of Leisa Lutz are Leslee Toombs, Eli Smock, Gene Smock.  ## Attributes The date of birth of Leisa Lutz is 1015-11-21.  The occupation of Leisa Lutz is clinical cytogeneticist.  The hobby of Leisa Lutz is geography.  The gender of Leisa Lutz is female.
Context9: # Isiah Lutz ## Family The son of Isiah Lutz is Lesley Lutz.  The wife of Isiah Lutz is Leisa Lutz.  ## Friends The friends of Isiah Lutz are Johnetta Wang, Ricardo Hackworth, Shelli Beltran, Stacia Toombs, Dominique Smock.  ## Attributes The date of birth of Isiah Lutz is 1014-10-18.  The occupation of Isiah Lutz is education administrator.  The hobby of Isiah Lutz is geocaching.  The gender of Isiah Lutz is male.
Context10: # Ryan Wang ## Family The daughter of Ryan Wang is Johnetta Wang.  The wife of Ryan Wang is Aida Wang.  ## Friends The friends of Ryan Wang are Shelli Beltran, Stacia Toombs, Virgil Hackworth, Aida Wang.  ## Attributes The date of birth of Ryan Wang is 0982-03-17.  The occupation of Ryan Wang is chief of staff.  The hobby of Ryan Wang is fossil hunting.  The gender of Ryan Wang is male.
Question: How many uncles does the friend of Stacia Toombs have?
Are follow up questions needed here: Yes.
Follow up: Who is the friend of Stacia Toombs?
Intermediate answer: The friends of Stacia Toombs are Brian Beltran, Isiah Lutz, Leeann Hackworth, Lesley Lutz, Ryan Wang.
Follow up: Who are the parents of Brian Beltran, Isiah Lutz, Leeann Hackworth, Lesley Lutz, Ryan Wang?
Intermediate answer: The parents of Brian Beltran are not provided. The parents of Isiah Lutz are not provided. The parents of Leeann Hackworth are Vicki Hackworth and Ricardo Hackworth. The parents of Lesley Lutz are Leisa Lutz and Isiah Lutz. The parents of Ryan Wang are not provided.
Follow up: Who are the brothers of Vicki Hackworth, Ricardo Hackworth, Leisa Lutz and Isiah Lutz?
Intermediate answer: The brothers of Vicki Hackworth are not provided. The brothers of Ricardo Hackworth are not provided. The brothers of Leisa Lutz are Virgil Hackworth. The brothers of Isiah Lutz are not provided.
So the final answer is: 0,1
"""