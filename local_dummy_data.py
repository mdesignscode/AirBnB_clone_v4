#!/usr/bin/python3
"""create some dummy data for file storage"""

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from os import remove
from datetime import datetime


# clear storage
try:
    remove('file.json')
except FileNotFoundError:
    pass


# create users
DustinHoffman = User(
    id='DustinHoffman',
    first_name='Dustin',
    last_name='Hoffman',
    email='oj@ifki.sx',
    password='1Oe9QL0S'
)
DustinHoffman.save()
JoseDiaz = User(
    id='JoseDiaz',
    first_name='Jose',
    last_name='Diaz',
    email='bavim@poki.hk',
    password='JruQacG3'
)
JoseDiaz.save()
CoraHolt = User(
    id='CoraHolt',
    first_name='Cora',
    last_name='Holt',
    email='CoraHolt@email.com',
    password='SAliJ9cx71uV'
)
CoraHolt.save()
GeorgeStewart = User(
    id='GeorgeStewart',
    first_name='George',
    last_name='Stewart',
    email='suhehedet@nec.tg',
    password='WSzWNUE5'
)
GeorgeStewart.save()
RubyWright = User(
    id='RubyWright',
    first_name='Ruby',
    last_name='Wright',
    email='RubyWright@email.com',
    password='iHnYyVDclUoLu1Pq'
)
RubyWright.save()
BradleyGross = User(
    id='BradleyGross',
    first_name='Bradley',
    last_name='Gross',
    email='BradleyGross@email.com',
    password='MlLxU0m1'
)
BradleyGross.save()
VincentGreer = User(
    id='VincentGreer',
    first_name='Vincent',
    last_name='Greer',
    email='VincentGreer@email.com',
    password='BtryUEyEOjti'
)
VincentGreer.save()
MariaDaniels = User(
    id='MariaDaniels',
    first_name='Maria',
    last_name='Daniels',
    email='MariaDaniels@email.com',
    password='7lP3Dty7'
)
MariaDaniels.save()

# create states
NewYork = State(id='NY', name='New York')
NewYork.save()
Florida = State(id='Florida', name='Florida')
Florida.save()
California = State(id='California', name='California')
California.save()

# create cities
LosAngeles = City(id='LosAngeles', name='Los Angeles', state_id='California')
LosAngeles.save()
Orlando = City(id='Orlando', name='Orlando', state_id='Florida')
Orlando.save()
Miami = City(id='Miami', name='Miami', state_id='Florida')
Miami.save()
NewYorkCity = City(id='NewYorkCity', name='New York City', state_id='NY')
NewYorkCity.save()
Albany = City(id='Albany', name='Albany', state_id='NY')
Albany.save()
FortMyers = City(id='FortMyers', name='Fort Myers', state_id='Florida')
FortMyers.save()
Tampa = City(id='Tampa', name='Tampa', state_id='Florida')
Tampa.save()
SanDiego = City(id='SanDiego', name='San Diego', state_id='California')
SanDiego.save()
CaliforniaCity = City(id='CaliforniaCity',
                      name='California City', state_id='California')
CaliforniaCity.save()

# create amenities
Wifi = Amenity(name='WiFi', id='WiFi')
Wifi.save()
Pool = Amenity(name='Pool', id='Pool')
Pool.save()
MobileCheckIn = Amenity(name='Mobile Check-In', id='MobileCheck-In')
MobileCheckIn.save()
Bar = Amenity(name='Bar', id='Bar')
Bar.save()
SmartTv = Amenity(name='SmartTv', id='SmartTv')
SmartTv.save()
RoomService = Amenity(name='Room Service', id='RoomService')
RoomService.save()
PetFriendly = Amenity(name='Pet Friendly', id='PetFriendly')
PetFriendly.save()
PoolBar = Amenity(name='Pool Bar', id='PoolBar')
PoolBar.save()
Restaurant = Amenity(name='On-site Restaurant', id='Restaurant')
Restaurant.save()
Robots = Amenity(name='AI Powered Robots', id='Robots')
Robots.save()
CocktailStation = Amenity(
    name='In-Room Cocktail Station', id='CocktailStation')
CocktailStation.save()
Casino = Amenity(name='Casino', id='Casino')
Casino.save()
Tech = Amenity(name='Enthusiast & Hobbyist Tech', id='Tech')
Tech.save()
HotelPetAmbassador = Amenity(
    name='Hotel Pet Ambassador', id='HotelPetAmbassador')
HotelPetAmbassador.save()

# create place
description = """
Autem qui quia veritatis fugiat tempore dignissimos sapiente minus neque. Id nostrum sint et id velit ut. Soluta perferendis ipsam inventore veniam dolores qui harum et distinctio.

Similique ut voluptatem dignissimos cumque. Adipisci quis ad et dolorem et nemo. Fugit error temporibus fugiat nobis. Nobis eligendi dolore possimus.

Et nulla cupiditate totam excepturi id ut a sed ullam. Minima delectus consequatur molestiae illo voluptas sunt. Omnis veniam voluptatem fuga nihil minus deleniti fugit unde quam. Magnam pariatur vitae rem autem similique.
"""
Yotel = Place(
    id='Yotel',
    city_id='NewYorkCity',
    user_id='DustinHoffman',
    name='Yotel',
    description=description,
    number_rooms=1,
    number_bathrooms=1,
    max_guest=2,
    price_by_night=104,
    longitude=58.6216,
    latitude=344.4797,
    amenity_ids=['WiFi', 'Pool', 'PetFriendly', 'HotelPetAmbassador']
)
Yotel.save()
description = """
Omnis commodi ut expedita. Molestiae itaque aut consequuntur veritatis molestiae ipsam illum maxime. Cum expedita consequatur fugiat illum dolorum. Pariatur ipsum aspernatur. Velit consectetur accusantium non debitis.

Est laborum quia eum. Nihil saepe est. Recusandae nobis cum rerum. Fugiat mollitia blanditiis rerum eos nulla expedita. Quibusdam doloribus magnam id ut sit adipisci esse tempora. Explicabo voluptas ab voluptates.

A ut expedita ut exercitationem suscipit et. Quo autem veniam odio autem molestias temporibus et. Laudantium voluptas quam vitae eum qui officia ipsam qui. Fuga sint voluptatem quam modi eaque sed corrupti.
"""
Marriott = Place(
    id='Marriott',
    city_id='Orlando',
    user_id='GeorgeStewart',
    name='Marriott',
    description=description,
    number_rooms=2,
    number_bathrooms=2,
    max_guest=4,
    price_by_night=311,
    longitude=92.1057,
    latitude=259.9597,
    amenity_ids=['PoolBar', 'CocktailStation', "Casino"]
)
Marriott.save()
description = """
Ut esse perspiciatis eligendi. Aliquam veritatis praesentium molestiae. Aut et vel consectetur quibusdam. Rem accusamus voluptatem est est iste distinctio id accusantium corporis.

Rerum temporibus ut. Modi qui et exercitationem maiores ipsam eius dolore occaecati laboriosam. Aut laborum omnis voluptas et fuga. Eos recusandae quis similique atque. Magnam qui dolor repudiandae suscipit et quia sed.

Doloremque ipsum est et. Voluptates eos et inventore est deleniti. Fugiat aut assumenda ut earum est accusantium accusantium repellendus. Fugit sed perspiciatis corporis quasi. Dolorem nulla id. Cum quos omnis sequi earum accusantium.
"""
HolidayInn = Place(
    id='HolidayInn',
    city_id='FortMyers',
    user_id='JoseDiaz',
    name='HolidayInn',
    description=description,
    number_rooms=3,
    number_bathrooms=3,
    max_guest=7,
    price_by_night=400,
    longitude=42.0188,
    latitude=38.183,
    amenity_ids=['WiFi', 'MobileCheck-In', 'Restaurant', 'Bar']
)
HolidayInn.save()
description = """
Et voluptas dicta voluptas eum id. Pariatur enim id quam voluptate consequatur aut ad. Repellendus aut voluptatem et ut velit. Neque voluptatem id adipisci asperiores sunt omnis fugit enim. Minima repudiandae quo quae tenetur et repudiandae ut.

Consectetur est sit consequuntur delectus. Assumenda rem in. Et non voluptatem cupiditate recusandae. Illum dignissimos vero molestiae aut autem ipsam est placeat in. Qui in natus autem perferendis unde. Doloribus fugit qui quas eum dolores sunt.

Eum ad perferendis ut dolorum eius cupiditate porro voluptatum. Harum aspernatur rerum ut sit ut delectus sed. Sed qui autem ea nam nulla laudantium id. Sit molestiae in illum eius eveniet ipsum veritatis omnis distinctio.
"""
Windham = Place(
    name='Hampton',
    city_id='Tampa',
    user_id='RubyWright',
    id='Windham',
    description=description,
    number_rooms=2,
    number_bathrooms=1,
    max_guest=4,
    price_by_night=201,
    longitude=104.6652,
    latitude=51.8682,
    amenity_ids=['Restaurant', 'RoomService', 'Robots', "MobileCheck-In"]
)
Windham.save()
description = """
Sint sapiente sed a quisquam voluptatem. Voluptas excepturi saepe accusamus quia rerum. Tenetur repellendus dolore. Quasi autem explicabo aut sequi ipsa atque iste et. Velit amet delectus assumenda magnam labore sed fuga.

Omnis ea aut est et eum nobis. Quae aperiam natus consequatur deserunt ea. Commodi cupiditate dolor vel autem beatae. In ipsum eveniet.

Sapiente aut eos voluptate deserunt. Repellat impedit veniam est voluptas. Quis sint animi incidunt. Modi et a voluptates sit quas odit.

Earum dolorum id iure ipsum optio placeat. Optio molestiae nostrum porro veritatis sapiente at maxime voluptatem. Corporis aspernatur voluptas quidem.
"""
Super8 = Place(
    name='Super 8',
    city_id='LosAngeles',
    user_id='BradleyGross',
    id='Super8',
    description=description,
    number_rooms=3,
    number_bathrooms=2,
    max_guest=6,
    price_by_night=356,
    longitude=104.6652,
    latitude=311.9097,
    amenity_ids=['WiFi', 'SmartTv', 'Tech', 'MobileCheck-In', 'Robots']
)
Super8.save()

# create reviews
Review1 = Review(
    user_id='MariaDaniels',
    place_id='Yotel',
    text='Eius occaecati exercitationem totam beatae aut in commodi.',
    id='Review1',
)
Review1.save()
Review2 = Review(user_id='VincentGreer',
                 place_id='Marriott',
                 text='Numquam adipisci est debitis.',
                 id='Review2'
                 )
Review2.save()
Review3 = Review(user_id='BradleyGross',
                 place_id='HolidayInn',
                 text='Et nisi sit inventore non.',
                 id='Review3'
                 )
Review3.save()
Review4 = Review(user_id='RubyWright',
                 place_id='Super8',
                 text='Et nisi sit inventore non corporis quasi voluptas.',
                 id='Review4'
                 )
Review4.save()
Review5 = Review(user_id='JoseDiaz',
                 place_id='Windham',
                 text='Maiores voluptas aliquam ducimus.',
                 id='Review5'
                 )
Review5.save()
Review6 = Review(user_id='CoraHolt',
                 place_id='Marriott',
                 text='Maiores voluptas aliquam ducimus.',
                 id='Review6'
                 )
Review6.save()
