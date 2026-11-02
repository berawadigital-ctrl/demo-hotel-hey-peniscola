# Contenido de la demo Hotel Hey (Peñíscola) (es/en/fr/de). Hechos de hotelhey.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Doble frontal vista mar','Doble lateral vista mar','Triple lateral vista mar'],'en':['Front double, sea view','Side double, sea view','Side triple, sea view'],'fr':['Double frontale vue mer','Double latérale vue mer','Triple latérale vue mer'],'de':['Doppelzimmer frontal, Meerblick','Doppelzimmer seitlich, Meerblick','Dreibettzimmer seitlich, Meerblick']}
RD={
'es':['Mirando de frente al mar, con terraza, aire acondicionado, nevera y baño privado con ducha.','Con terraza y vistas laterales al mar, aire acondicionado, nevera y baño privado.','Para tres, con cama supletoria, terraza con vistas al mar, aire acondicionado y nevera.'],
'en':['Facing the sea, with terrace, air conditioning, fridge and private bathroom with shower.','With terrace and side sea views, air conditioning, fridge and private bathroom.','For three, with an extra bed, sea-view terrace, air conditioning and fridge.'],
'fr':['Face à la mer, avec terrasse, climatisation, réfrigérateur et salle de bains privée avec douche.','Avec terrasse et vue latérale sur la mer, climatisation, réfrigérateur et salle de bains privée.','Pour trois, avec lit d’appoint, terrasse vue mer, climatisation et réfrigérateur.'],
'de':['Mit Blick direkt aufs Meer, Terrasse, Klimaanlage, Kühlschrank und eigenem Bad mit Dusche.','Mit Terrasse und seitlichem Meerblick, Klimaanlage, Kühlschrank und eigenem Bad.','Für drei Personen, mit Zustellbett, Terrasse mit Meerblick, Klimaanlage und Kühlschrank.']}
ART={
'hero':('waves',1811,['#10293a','#4a92b8','#e2f0f6','#3c6c82','#275468','#0b1d29']),
'intro':('skyline',1812,['#f6f2ea','#fbf9f4','#a0522d','#5f5850','#2e2a25']),
'r1':('waves',1821,['#10293a','#57a0c4','#e8f4f9','#457a91','#2c5c71','#0b1d29']),
'r2':('columns',1822,['#f6f2ea','#fbf9f4','#a0522d','#5f5850','#2e2a25']),
'r3':('arches',1823,['#eef5f7','#d5e7ee','#1e5f7e','#55626a','#1d2c34']),
'g1':('skyline',1831,['#10293a','#4a92b8','#e2f0f6','#3c6c82','#275468','#0b1d29']),
'g2':('hills',1832,['#f4efe4','#e8dcc4','#c9a87a','#9a8062','#735f48','#4b3d2f']),
'g3':('waves',1833,['#10293a','#57a0c4','#e8f4f9','#457a91','#2c5c71','#0b1d29']),
'g4':('columns',1834,['#f6f2ea','#fbf9f4','#a0522d','#5f5850','#2e2a25'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Hey · Hotel de playa en Peñíscola',see_rooms='Ver habitaciones',hero_k='Peñíscola · Avenida Valencia, 114',hero_t='Hotel en Peñíscola, en primera línea de playa',hero_s='A los pies de la playa de Peñíscola y a unos 1.500 m del Castillo del Papa Luna.',
 intro_t='Un hotel de playa para sentirte como en casa',intro_p1='Un hotel de 3 estrellas remodelado en su mayor parte: comedor, habitaciones, cafetería, recepción y piscina.',
 intro_p2='En El Restaurant Hey llevan más de 35 años preparando arroces y platos típicos de la forma más tradicional.',
 stats=['3 estrellas','Primera línea de playa','Piscina al aire libre','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con terraza o balcón con vistas al mar, aire acondicionado, nevera, TV por satélite y baño privado con secador y artículos de aseo.',
 svcs=['Piscina al aire libre','El Restaurant Hey, cocina mediterránea','Desayuno continental','Wifi gratuito en todo el hotel','Zona de lectura','Camas supletorias'],
 loc_p='Avenida Valencia, 114 · 12598 Peñíscola (Castellón). Teléfonos: 964 48 04 38 · 638 818 930. Correo: hey@hotelhey.com.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis piscina?','¿Hay desayuno?','¿Cómo reservo?']),
'en':dict(title='Hotel Hey · Beach hotel in Peñíscola',see_rooms='See rooms',hero_k='Peñíscola · Avenida Valencia, 114',hero_t='A beachfront hotel in Peñíscola',hero_s='Right by Peñíscola beach and about 1,500 m from the Castle of Pope Luna.',
 intro_t='A beach hotel that feels like home',intro_p1='A 3-star hotel largely refurbished: dining room, rooms, café, reception and pool.',
 intro_p2='At El Restaurant Hey they have been cooking rice dishes and local specialities the traditional way for over 35 years.',
 stats=['3 stars','Beachfront','Outdoor pool','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with a sea-view terrace or balcony, air conditioning, fridge, satellite TV and private bathroom with hairdryer and toiletries.',
 svcs=['Outdoor pool','El Restaurant Hey, Mediterranean cuisine','Continental breakfast','Free wifi throughout the hotel','Reading area','Extra beds'],
 loc_p='Avenida Valencia, 114 · 12598 Peñíscola (Castellón). Phones: +34 964 48 04 38 · +34 638 818 930. Email: hey@hotelhey.com.',
 chips=['Which rooms do you have?','Do you have a pool?','Is there breakfast?','How do I book?']),
'fr':dict(title='Hotel Hey · Hôtel de plage à Peñíscola',see_rooms='Voir les chambres',hero_k='Peñíscola · Avenida Valencia, 114',hero_t='Un hôtel en front de mer à Peñíscola',hero_s='Au pied de la plage de Peñíscola et à environ 1 500 m du château du pape Luna.',
 intro_t='Un hôtel de plage où l’on se sent chez soi',intro_p1='Un hôtel 3 étoiles en grande partie rénové : salle à manger, chambres, cafétéria, réception et piscine.',
 intro_p2='Au Restaurant Hey, on prépare depuis plus de 35 ans les riz et plats typiques de la manière la plus traditionnelle.',
 stats=['3 étoiles','Front de mer','Piscine extérieure','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec terrasse ou balcon vue mer, climatisation, réfrigérateur, TV satellite et salle de bains privée avec sèche-cheveux et produits d’accueil.',
 svcs=['Piscine extérieure','El Restaurant Hey, cuisine méditerranéenne','Petit-déjeuner continental','Wifi gratuit dans tout l’hôtel','Coin lecture','Lits d’appoint'],
 loc_p='Avenida Valencia, 114 · 12598 Peñíscola (Castellón). Téléphones : +34 964 48 04 38 · +34 638 818 930. E-mail : hey@hotelhey.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous une piscine ?','Y a-t-il un petit-déjeuner ?','Comment réserver ?']),
'de':dict(title='Hotel Hey · Strandhotel in Peñíscola',see_rooms='Zimmer ansehen',hero_k='Peñíscola · Avenida Valencia, 114',hero_t='Ein Hotel direkt am Strand von Peñíscola',hero_s='Am Strand von Peñíscola und etwa 1.500 m von der Burg des Papstes Luna.',
 intro_t='Ein Strandhotel, in dem Sie sich wie zu Hause fühlen',intro_p1='Ein 3-Sterne-Hotel, größtenteils renoviert: Speisesaal, Zimmer, Cafeteria, Rezeption und Pool.',
 intro_p2='Im El Restaurant Hey werden seit über 35 Jahren Reisgerichte und typische Speisen ganz traditionell zubereitet.',
 stats=['3 Sterne','Erste Strandlinie','Außenpool','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit Terrasse oder Balkon mit Meerblick, Klimaanlage, Kühlschrank, Satelliten-TV und eigenem Bad mit Föhn und Pflegeartikeln.',
 svcs=['Außenpool','El Restaurant Hey, mediterrane Küche','Kontinentales Frühstück','Kostenloses WLAN im ganzen Hotel','Leseecke','Zustellbetten'],
 loc_p='Avenida Valencia, 114 · 12598 Peñíscola (Castellón). Telefon: +34 964 48 04 38 · +34 638 818 930. E-Mail: hey@hotelhey.com.',
 chips=['Welche Zimmer gibt es?','Haben Sie einen Pool?','Gibt es Frühstück?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='hey@hotelhey.com')
D=dict(name='Hotel Hey',ac='#10293a',ac2='#1e5f7e',ac2_a11y='#1a5470',book=BOOK,around=[],foot=FOOT,
 address='Avenida Valencia, 114 · 12598 Peñíscola',phones=['+34 964 48 04 38','+34 638 818 930'],emails=['hey@hotelhey.com'],maps='Hotel Hey, Avenida Valencia 114, 12598 Peñíscola',t=T)
META=dict(repo='demo-hotel-hey-peniscola',name='Hotel Hey',legal_name='Hotel Hey S.L., CIF B12905550 (aviso legal de su web)',registry_ids=['B12905550'],
 url='https://www.hotelhey.com/',domain='hotelhey.com',municipality='Peñíscola',province='Castellón',sector='hotel de playa de 3 estrellas en Peñíscola',
 read_at='2026-11-02T10:59:00+01:00',created_at='2026-11-02T10:59:00+01:00',built_at='2026-11-02T11:25:00+01:00',audit_date='2026-11-02T10:59:00+01:00',
 rating=dict(value=4.2,coincide=['web'],date='2026-10-30',url='https://www.google.com/maps/search/Hotel+Hey+Pe%C3%B1%C3%ADscola'),
 book=dict(mode='mail',url='mailto:hey@hotelhey.com',note='sin motor de reservas: su web dice «Ponte en contacto con nosotros y consulta disponibilidad y tarifas por teléfono o email». Los botones Reservar de la demo abren un correo a hey@hotelhey.com y los telefonos reales 964 48 04 38 y 638 818 930 van en tel: (mismo criterio que San Martin y Andrin).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tenéis piscina?','K03'),('¿Hay desayuno?','K04'),('¿Tenéis restaurante?','K05'),('¿A qué hora es el check-in?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay wifi?','K09'),('¿Se puede fumar?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis camas supletorias?','K12'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Do you have a pool?','K03'),('Is there breakfast?','K04'),('Do you have a restaurant?','K05'),('What time is check-in?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there wifi?','K09'),('Can I smoke?','K10'),('What is your phone number?','K11'),('Do you have extra beds?','K12'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Avez-vous une piscine ?','K03'),('Y a-t-il un petit-déjeuner ?','K04'),('Avez-vous un restaurant ?','K05'),('À quelle heure est le check-in ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il le wifi ?','K09'),('Peut-on fumer ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous des lits d’appoint ?','K12'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Haben Sie einen Pool?','K03'),('Gibt es Frühstück?','K04'),('Haben Sie ein Restaurant?','K05'),('Wann ist der Check-in?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es WLAN?','K09'),('Darf man rauchen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie Zustellbetten?','K12'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
