from avg_img import avg_img
from img_scrape import scrape


#li = ['Mona Lisa', 'The Starry Night', 'The Scream', 'The Night Watch', 'The Kiss', 'The Arnolfini Portrait', 'The Girl With A Pearl Earring', 'Impression Sunrise', 'Las Meninas', 'The Creation Of Adam', 'Luncheon Of The Boating Party', 'The Grand Odalisque', 'The Swing', 'The Liberty Leading The People', 'The Birth Of Venus', 'Napoleon Crossing The Alps', 'Musicians', 'American Gothic', 'Sunday Afternoon On The Island Of La Grande Jatte', 'The Sleeping Gypsy', 'The Triumph Of Galatea', 'The Gleaners', 'Primavera', 'The Third Of May 1808', 'Charles I In Three Positions', 'The Wanderer Above The Sea Of Fog', 'Olympia', 'The Tower Of Babel', 'View Of Toledo', 'A Cotton Office In New Orleans', 'Bacchus And Ariadne', 'The Sleepers', 'The Gross Clinic', 'The Ninth Wave', 'The Last Supper', 'St. George And The Dragon', 'Mr And Mrs Robert Andrews', 'Pollice Verso', 'Pilgrimage To Cythera', 'Large Bathers', 'The Astronomer', 'Wave', 'The Fall Of The Damned', 'A Bar At The Folies Bergere', 'The Storm On The Sea Of Galilee', 'The Laughing Cavalier', 'Paris Street In Rainy Weather', 'Foxes', 'The Lady With The Ermine', 'Watson And The Shark', 'The Ladies Waldegrave', "Whistler's Mother", 'Dance At The Moulin De La Galette', 'Breezing Up', 'The Great Wave Off Kanagawa', 'Large Seated Nude', 'Stag Night At Sharkeys', 'The Night Cafe', 'The Avenue In The Rain', 'Annunciation', 'The Ambassadors', 'Flaming June', 'Susanna And The Elders', 'Composition VIII', 'The Oath Of Horatii', 'A Friend In Need', 'Dante And Virgil In Hell', 'Saturn Devouring His Son', 'Battle Of Issus', 'The Potato Eaters', 'The Birth Of Venus', 'Mars And Venus Allegory Of Peace', 'Red Balloon', 'The Lady Of Shalott', 'Portrait Of A Gentleman Skating', 'The Hay Wain', 'The Boat Trip', 'Sleeping Venus', 'Adoration Of The Magi', 'Portrait Of A Young Man', 'Boulevard Montmartre Spring', 'The Wedding At Cana', 'The Anatomy Lesson Of Dr. Nicolaes Tulp', 'The Raft Of The Medusa', 'The Kiss', 'The Bath', 'Fort Vimieux', 'The Japanese Bridge', 'Washington Crossing The Delaware', 'The Garden Of Earthly Delights', 'Supper At Emmaus', 'Feast Of The Rosary', 'The Hireling Shepherd', 'Hunters In The Snow', 'The Seed Of Areoi', 'Barge Haulers On The Volga', 'Odalisque', 'Cardsharps', 'The Pont Du Gard', 'The Luncheon On The Grass']

li = ['Andy Warhol', 'Pablo Picasso', 'Vincent van Gogh', 'Leonardo da Vinci', 'Michelangelo', 'Henri Matisse', 'Jackson Pollock', 'Edvard Munch', 'Claude Monet', 'Rene Magritte', 'Salvador Dalí', 'Edward Hopper', 'Frida Kahlo', 'Yayoi Kusama']


for piece in li:
    
    scrape(piece, warn = False)

    avg_img(1080, 1080, output = f'products/{piece}.jpg')
