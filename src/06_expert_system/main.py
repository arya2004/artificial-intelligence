import re # Used for cleaning user input

# --- 1. KNOWLEDGE BASE (Book Facts) ---
# A list of dictionaries representing the book facts from the Prolog file.
# Each book has 8 attributes: name, author, genre, language, year, publisher, length, age_group
BOOKS = [
    {'name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'fiction', 'language': 'english', 'year': 1960, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': "Harry Potter and the Sorcerer's Stone", 'author': 'J.K. Rowling', 'genre': 'fantasy', 'language': 'english', 'year': 1997, 'publisher': 'bloomsbury', 'length': 'long', 'age_group': 'teens'},
    {'name': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'fiction', 'language': 'english', 'year': 1925, 'publisher': 'scribner', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Alchemist', 'author': 'Paulo Coelho', 'genre': 'adventure', 'language': 'portuguese', 'year': 1988, 'publisher': 'harpercollins', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Don Quixote', 'author': 'Miguel de Cervantes', 'genre': 'adventure', 'language': 'spanish', 'year': 1605, 'publisher': 'francisco', 'length': 'long', 'age_group': 'adults'},
    {'name': 'War and Peace', 'author': 'Leo Tolstoy', 'genre': 'historical', 'language': 'russian', 'year': 1869, 'publisher': 'oxford', 'length': 'long', 'age_group': 'adults'},
    {'name': "Charlotte's Web", 'author': 'E.B. White', 'genre': 'kids', 'language': 'english', 'year': 1952, 'publisher': 'harpercollins', 'length': 'short', 'age_group': 'kids'},
    {'name': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'genre': 'fantasy', 'language': 'english', 'year': 1937, 'publisher': 'allen', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez', 'genre': 'magical_realism', 'language': 'spanish', 'year': 1967, 'publisher': 'harpercollins', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'romance', 'language': 'english', 'year': 1813, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Moby Dick', 'author': 'Herman Melville', 'genre': 'adventure', 'language': 'english', 'year': 1851, 'publisher': 'penguin', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Odyssey', 'author': 'Homer', 'genre': 'epic', 'language': 'greek', 'year': -800, 'publisher': 'oxford', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'genre': 'fiction', 'language': 'english', 'year': 1951, 'publisher': 'littlebrown', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Ulysses', 'author': 'James Joyce', 'genre': 'modernist', 'language': 'english', 'year': 1922, 'publisher': 'sylvia', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'genre': 'psychological', 'language': 'russian', 'year': 1866, 'publisher': 'penguin', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'dystopian', 'language': 'english', 'year': 1932, 'publisher': 'chatto', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Jane Eyre', 'author': 'Charlotte Bronte', 'genre': 'romance', 'language': 'english', 'year': 1847, 'publisher': 'smith', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Divine Comedy', 'author': 'Dante Alighieri', 'genre': 'epic', 'language': 'italian', 'year': 1320, 'publisher': 'penguin', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Brothers Karamazov', 'author': 'Fyodor Dostoevsky', 'genre': 'philosophical', 'language': 'russian', 'year': 1880, 'publisher': 'oxford', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'genre': 'fantasy', 'language': 'english', 'year': 1954, 'publisher': 'allen', 'length': 'long', 'age_group': 'teens'},
    {'name': 'The Metamorphosis', 'author': 'Franz Kafka', 'genre': 'absurdist', 'language': 'german', 'year': 1915, 'publisher': 'kurt', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'genre': 'philosophical', 'language': 'english', 'year': 1890, 'publisher': 'lippincott', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Frankenstein', 'author': 'Mary Shelley', 'genre': 'gothic', 'language': 'english', 'year': 1818, 'publisher': 'lackington', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Iliad', 'author': 'Homer', 'genre': 'epic', 'language': 'greek', 'year': -762, 'publisher': 'penguin', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Dracula', 'author': 'Bram Stoker', 'genre': 'horror', 'language': 'english', 'year': 1897, 'publisher': 'archibald', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'genre': 'dystopian', 'language': 'english', 'year': 1953, 'publisher': 'ballantine', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Anna Karenina', 'author': 'Leo Tolstoy', 'genre': 'romance', 'language': 'russian', 'year': 1877, 'publisher': 'oxford', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Grapes of Wrath', 'author': 'John Steinbeck', 'genre': 'fiction', 'language': 'english', 'year': 1939, 'publisher': 'viking', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Old Man and the Sea', 'author': 'Ernest Hemingway', 'genre': 'fiction', 'language': 'english', 'year': 1952, 'publisher': 'scribner', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Stranger', 'author': 'Albert Camus', 'genre': 'philosophical', 'language': 'french', 'year': 1942, 'publisher': 'gallimard', 'length': 'short', 'age_group': 'adults'},
    {'name': 'Les Misérables', 'author': 'Victor Hugo', 'genre': 'historical', 'language': 'french', 'year': 1862, 'publisher': 'pagnerre', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Lolita', 'author': 'Vladimir Nabokov', 'genre': 'psychological', 'language': 'english', 'year': 1955, 'publisher': 'olympia', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Sound and the Fury', 'author': 'William Faulkner', 'genre': 'modernist', 'language': 'english', 'year': 1929, 'publisher': 'jonathan', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Gone with the Wind', 'author': 'Margaret Mitchell', 'genre': 'historical', 'language': 'english', 'year': 1936, 'publisher': 'macmillan', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Wuthering Heights', 'author': 'Emily Bronte', 'genre': 'gothic', 'language': 'english', 'year': 1847, 'publisher': 'thomas', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Heart of Darkness', 'author': 'Joseph Conrad', 'genre': 'adventure', 'language': 'english', 'year': 1899, 'publisher': 'blackwood', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Bell Jar', 'author': 'Sylvia Plath', 'genre': 'fiction', 'language': 'english', 'year': 1963, 'publisher': 'harper', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Dune', 'author': 'Frank Herbert', 'genre': 'science_fiction', 'language': 'english', 'year': 1965, 'publisher': 'chilton', 'length': 'long', 'age_group': 'teens'},
    {'name': 'Catch-22', 'author': 'Joseph Heller', 'genre': 'satire', 'language': 'english', 'year': 1961, 'publisher': 'simon', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Road', 'author': 'Cormac McCarthy', 'genre': 'dystopian', 'language': 'english', 'year': 2006, 'publisher': 'knopf', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Time Machine', 'author': 'H.G. Wells', 'genre': 'science_fiction', 'language': 'english', 'year': 1895, 'publisher': 'heinemann', 'length': 'short', 'age_group': 'adults'},
    {'name': '1984', 'author': 'George Orwell', 'genre': 'dystopian', 'language': 'english', 'year': 1949, 'publisher': 'secker', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Slaughterhouse-Five', 'author': 'Kurt Vonnegut', 'genre': 'science_fiction', 'language': 'english', 'year': 1969, 'publisher': 'delacorte', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'A Clockwork Orange', 'author': 'Anthony Burgess', 'genre': 'dystopian', 'language': 'english', 'year': 1962, 'publisher': 'william', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Trial', 'author': 'Franz Kafka', 'genre': 'philosophical', 'language': 'german', 'year': 1925, 'publisher': 'kurt', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Beloved', 'author': 'Toni Morrison', 'genre': 'fiction', 'language': 'english', 'year': 1987, 'publisher': 'knopf', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Master and Margarita', 'author': 'Mikhail Bulgakov', 'genre': 'magical_realism', 'language': 'russian', 'year': 1967, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Kite Runner', 'author': 'Khaled Hosseini', 'genre': 'historical', 'language': 'english', 'year': 2003, 'publisher': 'riverhead', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Life of Pi', 'author': 'Yann Martel', 'genre': 'adventure', 'language': 'english', 'year': 2001, 'publisher': 'knopf', 'length': 'medium', 'age_group': 'adults'},
    {'name': "Midnight's Children", 'author': 'Salman Rushdie', 'genre': 'magical_realism', 'language': 'english', 'year': 1981, 'publisher': 'jonathan', 'length': 'long', 'age_group': 'adults'},
    {'name': "The Handmaid's Tale", 'author': 'Margaret Atwood', 'genre': 'dystopian', 'language': 'english', 'year': 1985, 'publisher': 'mcclelland', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson', 'genre': 'crime', 'language': 'swedish', 'year': 2005, 'publisher': 'norstedts', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Cloud Atlas', 'author': 'David Mitchell', 'genre': 'science_fiction', 'language': 'english', 'year': 2004, 'publisher': 'randomhouse', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Book Thief', 'author': 'Markus Zusak', 'genre': 'historical', 'language': 'english', 'year': 2005, 'publisher': 'knopf', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'The Shining', 'author': 'Stephen King', 'genre': 'horror', 'language': 'english', 'year': 1977, 'publisher': 'doubleday', 'length': 'long', 'age_group': 'adults'},
    {'name': 'It', 'author': 'Stephen King', 'genre': 'horror', 'language': 'english', 'year': 1986, 'publisher': 'viking', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Da Vinci Code', 'author': 'Dan Brown', 'genre': 'thriller', 'language': 'english', 'year': 2003, 'publisher': 'doubleday', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Hunger Games', 'author': 'Suzanne Collins', 'genre': 'dystopian', 'language': 'english', 'year': 2008, 'publisher': 'scholastic', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'The Fault in Our Stars', 'author': 'John Green', 'genre': 'romance', 'language': 'english', 'year': 2012, 'publisher': 'dutton', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'Twilight', 'author': 'Stephenie Meyer', 'genre': 'fantasy', 'language': 'english', 'year': 2005, 'publisher': 'littlebrown', 'length': 'long', 'age_group': 'teens'},
    {'name': 'Divergent', 'author': 'Veronica Roth', 'genre': 'dystopian', 'language': 'english', 'year': 2011, 'publisher': 'harpercollins', 'length': 'long', 'age_group': 'teens'},
    {'name': 'The Maze Runner', 'author': 'James Dashner', 'genre': 'dystopian', 'language': 'english', 'year': 2009, 'publisher': 'delacorte', 'length': 'long', 'age_group': 'teens'},
    {'name': "Ender's Game", 'author': 'Orson Scott Card', 'genre': 'science_fiction', 'language': 'english', 'year': 1985, 'publisher': 'tor', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'Ready Player One', 'author': 'Ernest Cline', 'genre': 'science_fiction', 'language': 'english', 'year': 2011, 'publisher': 'crown', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'The Giver', 'author': 'Lois Lowry', 'genre': 'dystopian', 'language': 'english', 'year': 1993, 'publisher': 'houghton', 'length': 'short', 'age_group': 'teens'},
    {'name': 'Percy Jackson & the Olympians: The Lightning Thief', 'author': 'Rick Riordan', 'genre': 'fantasy', 'language': 'english', 'year': 2005, 'publisher': 'hyperion', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'Eragon', 'author': 'Christopher Paolini', 'genre': 'fantasy', 'language': 'english', 'year': 2002, 'publisher': 'knopf', 'length': 'long', 'age_group': 'teens'},
    {'name': 'The Name of the Wind', 'author': 'Patrick Rothfuss', 'genre': 'fantasy', 'language': 'english', 'year': 2007, 'publisher': 'daw', 'length': 'long', 'age_group': 'teens'},
    {'name': 'The Curious Incident of the Dog in the Night-Time', 'author': 'Mark Haddon', 'genre': 'mystery', 'language': 'english', 'year': 2003, 'publisher': 'jonathan', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'Wonder', 'author': 'R.J. Palacio', 'genre': 'fiction', 'language': 'english', 'year': 2012, 'publisher': 'knopf', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Coraline', 'author': 'Neil Gaiman', 'genre': 'fantasy', 'language': 'english', 'year': 2002, 'publisher': 'harpercollins', 'length': 'short', 'age_group': 'kids'},
    {'name': 'Holes', 'author': 'Louis Sachar', 'genre': 'adventure', 'language': 'english', 'year': 1998, 'publisher': 'fsg', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe', 'author': 'C.S. Lewis', 'genre': 'fantasy', 'language': 'english', 'year': 1950, 'publisher': 'harpercollins', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Matilda', 'author': 'Roald Dahl', 'genre': 'fiction', 'language': 'english', 'year': 1988, 'publisher': 'viking', 'length': 'short', 'age_group': 'kids'},
    {'name': 'Charlie and the Chocolate Factory', 'author': 'Roald Dahl', 'genre': 'fiction', 'language': 'english', 'year': 1964, 'publisher': 'knopf', 'length': 'short', 'age_group': 'kids'},
    {'name': 'The BFG', 'author': 'Roald Dahl', 'genre': 'fantasy', 'language': 'english', 'year': 1982, 'publisher': 'jonathan', 'length': 'short', 'age_group': 'kids'},
    {'name': 'The Phantom Tollbooth', 'author': 'Norton Juster', 'genre': 'adventure', 'language': 'english', 'year': 1961, 'publisher': 'randomhouse', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Winnie-the-Pooh', 'author': 'A.A. Milne', 'genre': 'kids', 'language': 'english', 'year': 1926, 'publisher': 'methuen', 'length': 'short', 'age_group': 'kids'},
    {'name': 'Goodnight Moon', 'author': 'Margaret Wise Brown', 'genre': 'kids', 'language': 'english', 'year': 1947, 'publisher': 'harper', 'length': 'short', 'age_group': 'kids'},
    {'name': 'The Very Hungry Caterpillar', 'author': 'Eric Carle', 'genre': 'kids', 'language': 'english', 'year': 1969, 'publisher': 'penguin', 'length': 'short', 'age_group': 'kids'},
    {'name': 'Where the Wild Things Are', 'author': 'Maurice Sendak', 'genre': 'kids', 'language': 'english', 'year': 1963, 'publisher': 'harper', 'length': 'short', 'age_group': 'kids'},
    {'name': 'The Gruffalo', 'author': 'Julia Donaldson', 'genre': 'kids', 'language': 'english', 'year': 1999, 'publisher': 'macmillan', 'length': 'short', 'age_group': 'kids'},
    {'name': 'The Cat in the Hat', 'author': 'Dr. Seuss', 'genre': 'kids', 'language': 'english', 'year': 1957, 'publisher': 'randomhouse', 'length': 'short', 'age_group': 'kids'},
    {'name': "Alice's Adventures in Wonderland", 'author': 'Lewis Carroll', 'genre': 'fantasy', 'language': 'english', 'year': 1865, 'publisher': 'macmillan', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Peter Pan', 'author': 'J.M. Barrie', 'genre': 'fantasy', 'language': 'english', 'year': 1911, 'publisher': 'hodder', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'The Wind in the Willows', 'author': 'Kenneth Grahame', 'genre': 'fantasy', 'language': 'english', 'year': 1908, 'publisher': 'methuen', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'The Secret Garden', 'author': 'Frances Hodgson Burnett', 'genre': 'fiction', 'language': 'english', 'year': 1911, 'publisher': 'harper', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Anne of Green Gables', 'author': 'L.M. Montgomery', 'genre': 'fiction', 'language': 'english', 'year': 1908, 'publisher': 'lothrop', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Little Women', 'author': 'Louisa May Alcott', 'genre': 'fiction', 'language': 'english', 'year': 1868, 'publisher': 'roberts', 'length': 'long', 'age_group': 'teens'},
    {'name': 'The Call of the Wild', 'author': 'Jack London', 'genre': 'adventure', 'language': 'english', 'year': 1903, 'publisher': 'macmillan', 'length': 'short', 'age_group': 'adults'},
    {'name': 'Treasure Island', 'author': 'Robert Louis Stevenson', 'genre': 'adventure', 'language': 'english', 'year': 1883, 'publisher': 'cassell', 'length': 'medium', 'age_group': 'kids'},
    {'name': 'Robinson Crusoe', 'author': 'Daniel Defoe', 'genre': 'adventure', 'language': 'english', 'year': 1719, 'publisher': 'william', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Black Beauty', 'author': 'Anna Sewell', 'genre': 'fiction', 'language': 'english', 'year': 1877, 'publisher': 'jarrold', 'length': 'medium', 'age_group': 'kids'},
    {'name': "Gulliver's Travels", 'author': 'Jonathan Swift', 'genre': 'adventure', 'language': 'english', 'year': 1726, 'publisher': 'benj', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Scarlet Letter', 'author': 'Nathaniel Hawthorne', 'genre': 'fiction', 'language': 'english', 'year': 1850, 'publisher': 'ticknor', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Of Mice and Men', 'author': 'John Steinbeck', 'genre': 'fiction', 'language': 'english', 'year': 1937, 'publisher': 'covici', 'length': 'short', 'age_group': 'adults'},
    {'name': 'A Tale of Two Cities', 'author': 'Charles Dickens', 'genre': 'historical', 'language': 'english', 'year': 1859, 'publisher': 'chapman', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'David Copperfield', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1850, 'publisher': 'bradbury', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Oliver Twist', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1837, 'publisher': 'bentley', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Great Expectations', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1861, 'publisher': 'chapman', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Hard Times', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1854, 'publisher': 'bradbury', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'A Christmas Carol', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1843, 'publisher': 'chapman', 'length': 'short', 'age_group': 'adults'},
    {'name': 'Bleak House', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1853, 'publisher': 'bradbury', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Hound of the Baskervilles', 'author': 'Arthur Conan Doyle', 'genre': 'mystery', 'language': 'english', 'year': 1902, 'publisher': 'george', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Adventures of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'genre': 'mystery', 'language': 'english', 'year': 1892, 'publisher': 'george', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Three Musketeers', 'author': 'Alexandre Dumas', 'genre': 'adventure', 'language': 'french', 'year': 1844, 'publisher': 'baudry', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Count of Monte Cristo', 'author': 'Alexandre Dumas', 'genre': 'adventure', 'language': 'french', 'year': 1844, 'publisher': 'baudry', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Man in the Iron Mask', 'author': 'Alexandre Dumas', 'genre': 'adventure', 'language': 'french', 'year': 1850, 'publisher': 'baudry', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Phantom of the Opera', 'author': 'Gaston Leroux', 'genre': 'horror', 'language': 'french', 'year': 1910, 'publisher': 'pierre', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Journey to the Center of the Earth', 'author': 'Jules Verne', 'genre': 'science_fiction', 'language': 'french', 'year': 1864, 'publisher': 'pierre', 'length': 'medium', 'age_group': 'teens'},
    {'name': 'Twenty Thousand Leagues Under the Sea', 'author': 'Jules Verne', 'genre': 'science_fiction', 'language': 'french', 'year': 1870, 'publisher': 'pierre', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Around the World in Eighty Days', 'author': 'Jules Verne', 'genre': 'adventure', 'language': 'french', 'year': 1873, 'publisher': 'hetzel', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The War of the Worlds', 'author': 'H.G. Wells', 'genre': 'science_fiction', 'language': 'english', 'year': 1898, 'publisher': 'heinemann', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Invisible Man', 'author': 'H.G. Wells', 'genre': 'science_fiction', 'language': 'english', 'year': 1897, 'publisher': 'cockerell', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Island of Doctor Moreau', 'author': 'H.G. Wells', 'genre': 'science_fiction', 'language': 'english', 'year': 1896, 'publisher': 'heinemann', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Brave New World Revisited', 'author': 'Aldous Huxley', 'genre': 'dystopian', 'language': 'english', 'year': 1958, 'publisher': 'chatto', 'length': 'short', 'age_group': 'adults'},
    {'name': 'A Room with a View', 'author': 'E.M. Forster', 'genre': 'romance', 'language': 'english', 'year': 1908, 'publisher': 'edward', 'length': 'medium', 'age_group': 'adults'},
    {'name': "Howard's End", 'author': 'E.M. Forster', 'genre': 'fiction', 'language': 'english', 'year': 1910, 'publisher': 'edward', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Remains of the Day', 'author': 'Kazuo Ishiguro', 'genre': 'fiction', 'language': 'english', 'year': 1989, 'publisher': 'faber', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'White Teeth', 'author': 'Zadie Smith', 'genre': 'fiction', 'language': 'english', 'year': 2000, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'On the Road', 'author': 'Jack Kerouac', 'genre': 'fiction', 'language': 'english', 'year': 1957, 'publisher': 'viking', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Sun Also Rises', 'author': 'Ernest Hemingway', 'genre': 'fiction', 'language': 'english', 'year': 1926, 'publisher': 'scribner', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'For Whom the Bell Tolls', 'author': 'Ernest Hemingway', 'genre': 'fiction', 'language': 'english', 'year': 1940, 'publisher': 'scribner', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Old Curiosity Shop', 'author': 'Charles Dickens', 'genre': 'fiction', 'language': 'english', 'year': 1841, 'publisher': 'chapman', 'length': 'long', 'age_group': 'adults'},
    {'name': 'To the Lighthouse', 'author': 'Virginia Woolf', 'genre': 'modernist', 'language': 'english', 'year': 1927, 'publisher': 'hogarth', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Mrs Dalloway', 'author': 'Virginia Woolf', 'genre': 'modernist', 'language': 'english', 'year': 1925, 'publisher': 'hogarth', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Orlando', 'author': 'Virginia Woolf', 'genre': 'modernist', 'language': 'english', 'year': 1928, 'publisher': 'hogarth', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Waves', 'author': 'Virginia Woolf', 'genre': 'modernist', 'language': 'english', 'year': 1931, 'publisher': 'hogarth', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Trial of Socrates', 'author': 'I.F. Stone', 'genre': 'philosophical', 'language': 'english', 'year': 1988, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Republic', 'author': 'Plato', 'genre': 'philosophical', 'language': 'greek', 'year': -375, 'publisher': 'penguin', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Thus Spoke Zarathustra', 'author': 'Friedrich Nietzsche', 'genre': 'philosophical', 'language': 'german', 'year': 1883, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Prince', 'author': 'Niccolo Machiavelli', 'genre': 'political', 'language': 'italian', 'year': 1532, 'publisher': 'antonio', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Communist Manifesto', 'author': 'Karl Marx', 'genre': 'political', 'language': 'german', 'year': 1848, 'publisher': 'engels', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Wealth of Nations', 'author': 'Adam Smith', 'genre': 'economics', 'language': 'english', 'year': 1776, 'publisher': 'william', 'length': 'long', 'age_group': 'adults'},
    {'name': 'Capital', 'author': 'Karl Marx', 'genre': 'political', 'language': 'german', 'year': 1867, 'publisher': 'otto', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Art of War', 'author': 'Sun Tzu', 'genre': 'strategy', 'language': 'chinese', 'year': -500, 'publisher': 'penguin', 'length': 'short', 'age_group': 'adults'},
    {'name': 'The Art of Happiness', 'author': 'Dalai Lama', 'genre': 'philosophical', 'language': 'english', 'year': 1998, 'publisher': 'riverhead', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Siddhartha', 'author': 'Hermann Hesse', 'genre': 'philosophical', 'language': 'german', 'year': 1922, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Power of Now', 'author': 'Eckhart Tolle', 'genre': 'self_help', 'language': 'english', 'year': 1997, 'publisher': 'newworld', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Road Less Traveled', 'author': 'M. Scott Peck', 'genre': 'self_help', 'language': 'english', 'year': 1978, 'publisher': 'simon', 'length': 'medium', 'age_group': 'adults'},
    {'name': "Man's Search for Meaning", 'author': 'Viktor Frankl', 'genre': 'self_help', 'language': 'english', 'year': 1946, 'publisher': 'beacon', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Seven Habits of Highly Effective People', 'author': 'Stephen Covey', 'genre': 'self_help', 'language': 'english', 'year': 1989, 'publisher': 'simon', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Power of Positive Thinking', 'author': 'Norman Vincent Peale', 'genre': 'self_help', 'language': 'english', 'year': 1952, 'publisher': 'simon', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'How to Win Friends and Influence People', 'author': 'Dale Carnegie', 'genre': 'self_help', 'language': 'english', 'year': 1936, 'publisher': 'simon', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Think and Grow Rich', 'author': 'Napoleon Hill', 'genre': 'self_help', 'language': 'english', 'year': 1937, 'publisher': 'ballou', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Four Agreements', 'author': 'Don Miguel Ruiz', 'genre': 'self_help', 'language': 'english', 'year': 1997, 'publisher': 'amberallen', 'length': 'short', 'age_group': 'adults'},
    {'name': 'Atomic Habits', 'author': 'James Clear', 'genre': 'self_help', 'language': 'english', 'year': 2018, 'publisher': 'penguin', 'length': 'medium', 'age_group': 'adults'},
    {'name': "Quiet: The Power of Introverts in a World That Can't Stop Talking", 'author': 'Susan Cain', 'genre': 'self_help', 'language': 'english', 'year': 2012, 'publisher': 'crown', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Subtle Art of Not Giving a F*ck', 'author': 'Mark Manson', 'genre': 'self_help', 'language': 'english', 'year': 2016, 'publisher': 'harper', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Educated', 'author': 'Tara Westover', 'genre': 'memoir', 'language': 'english', 'year': 2018, 'publisher': 'randomhouse', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Becoming', 'author': 'Michelle Obama', 'genre': 'memoir', 'language': 'english', 'year': 2018, 'publisher': 'crown', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'The Glass Castle', 'author': 'Jeannette Walls', 'genre': 'memoir', 'language': 'english', 'year': 2005, 'publisher': 'scribner', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Wild', 'author': 'Cheryl Strayed', 'genre': 'memoir', 'language': 'english', 'year': 2012, 'publisher': 'knopf', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Born a Crime', 'author': 'Trevor Noah', 'genre': 'memoir', 'language': 'english', 'year': 2016, 'publisher': 'spiegel', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Steve Jobs', 'author': 'Walter Isaacson', 'genre': 'biography', 'language': 'english', 'year': 2011, 'publisher': 'simon', 'length': 'long', 'age_group': 'adults'},
    {'name': 'The Wright Brothers', 'author': 'David McCullough', 'genre': 'biography', 'language': 'english', 'year': 2015, 'publisher': 'simon', 'length': 'medium', 'age_group': 'adults'},
    {'name': 'Alexander Hamilton', 'author': 'Ron Chernow', 'genre': 'biography', 'language': 'english', 'year': 2004, 'publisher': 'penguin', 'length': 'long', 'age_group': 'adults'},
]

# A list of book attribute keys for easy iteration during scoring
ATTRIBUTE_KEYS = ['author', 'genre', 'language', 'year', 'publisher', 'length', 'age_group']

# --- 2. LOGIC FUNCTIONS (Prolog Predicate Conversion) ---

def process_input(prompt_text):
    """Handles user input, converts to lowercase, and strips extra spaces."""
    user_input = input(prompt_text).strip()
    return user_input.lower()

def compare_attribute(val1, val2):
    """
    Corresponds to compare_attribute/3 in Prolog.
    Compares two string attributes. Returns 1 for a match, 0 otherwise.
    Handles 'any' input by returning 1 (always a match).
    """
    if val1 == 'any' or val2 == 'any':
        return 1.0
    if val1 == val2:
        return 1.0
    return 0.0

def compare_year(year1, year2):
    """
    Corresponds to compare_year/3 in Prolog.
    Compares two year attributes.
    Returns 1.0 if years are equal or if one is 'any'.
    Returns 0.5 if years are within 5 years of each other.
    Returns 0.0 otherwise.
    """
    # If the user selected 'any' for year
    if year1 == 'any' or year2 == 'any':
        return 1.0

    try:
        y1 = int(year1)
        y2 = int(year2)
    except ValueError:
        # If one of the comparison years is not a valid integer (shouldn't happen for BOOKS data)
        return 0.0

    if y1 == y2:
        return 1.0
    if abs(y1 - y2) <= 5:
        return 0.5
    return 0.0

def calculate_similarity_score(pref_attributes, book_attributes):
    """
    Corresponds to similarity_score/3 in Prolog.
    Calculates the total similarity score between a user's preference profile
    (or a previous book's attributes) and a specific book's attributes.

    Args:
        pref_attributes (dict): The target attributes (from user input or a source book).
        book_attributes (dict): The attributes of the book being scored.

    Returns:
        float: The total similarity score.
    """
    score = 0.0

    # Attributes that use the simple compare_attribute logic
    for key in ['author', 'genre', 'language', 'publisher', 'length', 'age_group']:
        score += compare_attribute(pref_attributes[key], book_attributes[key])

    # Special handling for 'year' using compare_year logic
    score += compare_year(pref_attributes['year'], book_attributes['year'])

    return score

def find_best_match(target_attributes, exclude_book_name=None):
    """
    The core recommendation engine. Finds the book with the highest similarity score.

    Args:
        target_attributes (dict): The profile (either a user profile or a source book profile)
                                  to match against.
        exclude_book_name (str, optional): Name of a book to exclude from results.

    Returns:
        str: The name of the best matching book, or None if no match is found.
    """
    ranked_books = []

    for book in BOOKS:
        # Exclude the book if it matches the exclusion name
        if exclude_book_name and book['name'].lower() == exclude_book_name.lower():
            continue

        score = calculate_similarity_score(target_attributes, book)
        ranked_books.append((book['name'], score))

    # Sort in descending order by score (the second element of the tuple)
    ranked_books.sort(key=lambda item: item[1], reverse=True)

    # Return the name of the top-ranked book
    if ranked_books and ranked_books[0][1] > 0:
        return ranked_books[0][0]
    return None

# --- 3. USER INTERACTION FUNCTIONS ---

def get_book_by_name(name):
    """Helper to retrieve a book's attributes by its name."""
    clean_name = name.lower()
    for book in BOOKS:
        if book['name'].lower() == clean_name:
            # We clone the attributes to prevent accidental modification of the global list
            return {k: str(v).lower() if isinstance(v, str) else v for k, v in book.items()}
    return None

def ask_previous_book():
    """Corresponds to ask_previous_book/1 in Prolog."""
    print('\nDo you want recommendations based on a previously read book?')
    user_input = process_input('(Type the **exact** book name or "none"): ')

    # Sanitize book name input
    cleaned_input = re.sub(r'[^a-zA-Z0-9\s:\-\'&,]', '', user_input.replace("'", ""))

    if cleaned_input == 'none':
        return 'none'
    
    # Check if the book exists in the knowledge base
    book_match = get_book_by_name(cleaned_input)
    if book_match:
        # Return the original, properly cased name for lookup consistency in get_book_by_name
        return book_match['name']
    
    print(f"Error: Book '{user_input}' not found in our database.")
    return 'none' # Fall back to preference-based recommendation if book is not found

def ask_author():
    return process_input('Do you have a preferred author? (Type the name or "any"): ')

def ask_genre():
    return process_input('What genre do you prefer? (e.g., fiction, fantasy, romance, or "any"): ')

def ask_language():
    return process_input('Do you have a preferred language? (e.g., english, spanish, or "any"): ')

def ask_year():
    year_input = process_input('Any preferred publication year? (Enter year or "any"): ')
    if year_input.lower() == 'any':
        return 'any'
    try:
        # Convert to string for consistent dictionary access later, but keep as a number if valid
        return int(year_input)
    except ValueError:
        print("Invalid year format. Defaulting to 'any'.")
        return 'any'

def ask_publisher():
    return process_input('Any preferred publisher? (Type the name or "any"): ')

def ask_length():
    return process_input('Do you prefer short, medium, or long books? (Type or "any"): ')

def ask_age_group():
    return process_input('For what age group are you looking for? (kids, teens, adults, or "any"): ')

# --- 4. MAIN APPLICATION ---

def recommend_books():
    """
    The main control function, corresponding to recommend_books/0 in Prolog.
    Orchestrates the user interaction and recommendation process.
    """
    print('=' * 50)
    print('-------------------------------------------')
    print('Welcome to the Book Recommendation System!')
    print('-------------------------------------------')
    print('Please answer the following questions to get a book recommendation.')
    print('=' * 50)

    # 1. Ask about a previous book
    previous_book_name = ask_previous_book()

    if previous_book_name != 'none':
        # --- PATH 1: Recommend Similar Book (Similar to recommend_similar_book/1) ---
        print('\n--- Finding Similar Book ---')
        
        # Get the attributes of the source book
        source_book_data = get_book_by_name(previous_book_name)

        if not source_book_data:
            print("Could not find the details for that book. Falling back to preference-based recommendation.")
            # Fall through to the preference-based path
        else:
            # Find the best match, excluding the source book itself
            recommended_book = find_best_match(source_book_data, exclude_book_name=previous_book_name)

            if recommended_book:
                print(f'\nBased on reading **{previous_book_name}**, we recommend: **{recommended_book}**')
            else:
                print('Sorry, we could not find a closely similar book for you.')
            return # End application after a successful similar recommendation

    # --- PATH 2: Preference-Based Recommendation (Similar to find_books/7) ---
    print('\n--- Gathering Preferences for New Recommendation ---')
    
    # Gather all attributes from the user
    user_preferences = {
        'author': ask_author(),
        'genre': ask_genre(),
        'language': ask_language(),
        'year': ask_year(),
        'publisher': ask_publisher(),
        'length': ask_length(),
        'age_group': ask_age_group(),
    }
    
    # Find the best match based on the user's preference profile
    recommended_book = find_best_match(user_preferences)

    print('\n' + '=' * 50)
    if recommended_book:
        print(f"Here is the recommended book based on your preferences: **{recommended_book}**")
    else:
        print('No books match your preferences. Try running again with more "any" options!')
    print('=' * 50)

# Run the main function if the script is executed directly
if __name__ == '__main__':
    recommend_books()
