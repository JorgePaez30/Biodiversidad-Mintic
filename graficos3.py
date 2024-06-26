import pandas as pd
import matplotlib.pyplot as plt

cadenajson=[
    {"Tipo":"Plantas","Nombre_Comun":"Violeta Africana","Nombre_Cientifico":"Alloplectus","Habitat":"Va Fusagasuga - San Miguel, Silvania, Cundinamarca","Latitud":	4.4100333333	,"Longitud":	-74.3260633333	,"Altitud":	1765	,"imagen":"https://static.inaturalist.org/photos/392833773/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/221805438"},
	{"Tipo":"Mamifero","Nombre_Comun":"Mono Aullador Rojo","Nombre_Cientifico":"Alouatta seniculus","Habitat":"Paratebueno, Cundinamarca","Latitud":	4.36581	,"Longitud":	-73.28906	,"Altitud":	256	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/278876677/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/161343866"},
	{"Tipo":"Plantas","Nombre_Comun":"Amancay","Nombre_Cientifico":"Alstroemeria aurea","Habitat":"Mercenaria, Sopo, Cundinamarca","Latitud":	4.8456333333	,"Longitud":	-73.9750283333	,"Altitud":	2650	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/393052349/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/221923098"},
	{"Tipo":"Reptil","Nombre_Comun":"Camaleon de Paramo","Nombre_Cientifico":"Anolis heterodermus","Habitat":"Gachantiva, Boyaca","Latitud":	5.7424521027	,"Longitud":	-73.5206900595	,"Altitud":	2450	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/249654155/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/145356519"},
	{"Tipo":"Reptil","Nombre_Comun":"Lagarto Jesucristo de Cabeza Roja","Nombre_Cientifico":"Basiliscus galeritus","Habitat":"La Maquina, Pacho, Cundinamarca","Latitud":	5.1461028333	,"Longitud":	-74.2053466667	,"Altitud":	2136	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/389491476/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/220016578"},
	{"Tipo":"Ave","Nombre_Comun":"Esmeralda Colicorta","Nombre_Cientifico":"Chlorostilbon poortmani","Habitat":"Gachantiva, Boyaca","Latitud":	5.7424324587	,"Longitud":	-73.5206573471	,"Altitud":	2450	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/364241173/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/205965887"},
	{"Tipo":"Mamifero","Nombre_Comun":"Perezoso de Dos Dedos","Nombre_Cientifico":"Choloepus hoffmanni","Habitat":"Sasaima, Cundinamarca","Latitud":	4.9638805556	,"Longitud":	-74.4343916667	,"Altitud":	1126	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/362959330/original.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/205284071"},
	{"Tipo":"Mamifero","Nombre_Comun":"Puercoespin","Nombre_Cientifico":"Coendou vestitus","Habitat":"Reserva Natural Los Yataros, Boyaca","Latitud":	5.7881428925	,"Longitud":	-73.5508596897	,"Altitud":	2200	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/165890985/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/99506008"},
	{"Tipo":"Insecto","Nombre_Comun":"Mosca Metalica Rayada","Nombre_Cientifico":"Condylostylus occidentalis","Habitat":"Choachi, Cundinamarca","Latitud":	4.5286591235	,"Longitud":	-73.9229679108	,"Altitud":	1921	,"imagen":"https://static.inaturalist.org/photos/392984077/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221887068"},
	{"Tipo":"Ave","Nombre_Comun":"Chimachima","Nombre_Cientifico":"Daptrius chimachima","Habitat":"Choachi, Cundinamarca","Latitud":	4.6089379537	,"Longitud":	-73.9014312528	,"Altitud":	1924	,"imagen":"https://static.inaturalist.org/photos/392858627/original.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221822188"},
	{"Tipo":"Ave","Nombre_Comun":"Chimachima","Nombre_Cientifico":"Daptrius chimachima","Habitat":"Tunja, Boyaca","Latitud":	5.5512859017	,"Longitud":	-73.3573734184	,"Altitud":	2820	,"imagen":"https://static.inaturalist.org/photos/387193049/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/218788436"},
	{"Tipo":"Mamifero","Nombre_Comun":"Armadillo de Nueve Bandas","Nombre_Cientifico":"Dasypus novemcinctus","Habitat":"Susacon, Boyaca","Latitud":	6.22380426	,"Longitud":	-72.69103061	,"Altitud":	2480	,"imagen":"https://static.inaturalist.org/photos/8707613/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/6837518"},
	{"Tipo":"Anfibio","Nombre_Comun":"Rana Venenosa de Rayas Amarillas","Nombre_Cientifico":"Dendrobates truncatus","Habitat":"Versalles, Guaduas, Cundinamarca","Latitud":	5.1276278333	,"Longitud":	-74.5927416667	,"Altitud":	992	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/360640333/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/204065588"},
	{"Tipo":"Anfibio","Nombre_Comun":"Rana Sabanera","Nombre_Cientifico":"Dendropsophus molitor","Habitat":"Samaca, Boyaca","Latitud":	5.4636524399	,"Longitud":	-73.5475740251	,"Altitud":	2660	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/170868740/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/102242537"},
	{"Tipo":"Plantas","Nombre_Comun":"Amor Seco","Nombre_Cientifico":"Desmodium molliculum","Habitat":"Gachantiva, Boyaca","Latitud":	5.7048718916	,"Longitud":	-73.563871254	,"Altitud":	2450	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/390137255/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/220361439"},
	{"Tipo":"Reptil","Nombre_Comun":"Lagarto Arcoiris","Nombre_Cientifico":"Diploglossus monotropis","Habitat":"Muzo, Boyaca","Latitud":	5.5461201521	,"Longitud":	-74.1047599912	,"Altitud":	815	,"imagen":"https://static.inaturalist.org/photos/333244643/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/190134441"},
	{"Tipo":"Ave","Nombre_Comun":"Carpintero Lineado","Nombre_Cientifico":"Dryocopus lineatus","Habitat":"La Mesa, Cundinamarca","Latitud":	4.6926193871	,"Longitud":	-74.4247182559	,"Altitud":	1200	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/388403060/original.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/219436087"},
	{"Tipo":"Plantas","Nombre_Comun":"Acantos, Flores de Camarn, Muites Y Parientes","Nombre_Cientifico":"Familia Acanthaceae","Habitat":"Viani, Cundinamarca","Latitud":	4.849602	,"Longitud":	-74.5662835	,"Altitud":	1498	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/391344278/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221005372"},
	{"Tipo":"Insecto","Nombre_Comun":"Avispas Icneumnidas","Nombre_Cientifico":"Familia Ichneumonidae","Habitat":"Bojaca, Cundinamarca","Latitud":	4.6962355941	,"Longitud":	-74.3602104002	,"Altitud":	2598	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/393024464/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221911163"},
	{"Tipo":"Reptil","Nombre_Comun":"Cuijes, Huicos Y Parientes","Nombre_Cientifico":"Familia Teiidae","Habitat":"Puerto Boyac, Boyaca","Latitud":	5.9834094444	,"Longitud":	-74.5614707842	,"Altitud":	145	,"imagen":"https://static.inaturalist.org/photos/355843372/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/201568975"},
	{"Tipo":"Insecto","Nombre_Comun":"Chicharras","Nombre_Cientifico":"genero Amphipsalta","Habitat":"Villa de Leyva, Boyaca","Latitud":	5.636499	,"Longitud":	-73.527058	,"Altitud":	2149	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/375200930/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/212311549"},
	{"Tipo":"Anfibio","Nombre_Comun":"Ranas Grillo Enanas","Nombre_Cientifico":"genero Dendropsophus","Habitat":"Moniquirá, Boyacá","Latitud":	5.9025199556	,"Longitud":	-73.5526487231	,"Altitud":	1669	,"imagen":"https://static.inaturalist.org/photos/168704381/original.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/101041376"},
	{"Tipo":"Mamifero","Nombre_Comun":"Tlacuaches, Zarigüeyas o Chuchas","Nombre_Cientifico":"genero Didelphis","Habitat":"Sue Reserva del Cacique, Sector Laguna Sagrada, Vereda Cacique, Ubaque, Cundinamarca","Latitud":	4.4963812	,"Longitud":	-73.9336195	,"Altitud":	1867	,"imagen":"https://static.inaturalist.org/photos/375189149/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/212305597"},
	{"Tipo":"Insecto","Nombre_Comun":"Abejas del Celofan","Nombre_Cientifico":"gnero Colletes","Habitat":"Nocaima, Cundinamarca","Latitud":	5.069434873	,"Longitud":	-74.3803049996	,"Altitud":	1200	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/392205044/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221467710"},
	{"Tipo":"Mamifero","Nombre_Comun":"Murcielagos Orejas de Raton","Nombre_Cientifico":"gnero Myotis","Habitat":"Moniquira, Boyaca","Latitud":	5.9181334732	,"Longitud":	-73.6037142453	,"Altitud":	1669	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/316064565/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/181379986"},
	{"Tipo":"Reptil","Nombre_Comun":"Falsa Coralillo Real Sudamericana","Nombre_Cientifico":"Lampropeltis micropholis","Habitat":"San Francisco, Cundinamarca","Latitud":	4.9878488652	,"Longitud":	-74.2763378844	,"Altitud":	1641	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/362625324/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/205111935"},
	{"Tipo":"Ave","Nombre_Comun":"Siriri Bueyero","Nombre_Cientifico":"Machetornis rixosa","Habitat":"Choachi, Cundinamarca","Latitud":	4.5585115845	,"Longitud":	-73.9086397193	,"Altitud":	1924	,"imagen":"https://static.inaturalist.org/photos/392858550/original.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221822178"},
	{"Tipo":"Ave","Nombre_Comun":"Siriri Bueyero","Nombre_Cientifico":"Machetornis rixosa","Habitat":"Cinega, Boyaca","Latitud":	5.4127293408	,"Longitud":	-73.3063062653	,"Altitud":	2463	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/390893565/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/220765324"},
	{"Tipo":"Mamifero","Nombre_Comun":"Comadreja Cola Larga","Nombre_Cientifico":"Neogale frenata","Habitat":"Tocancipa, Cundinamarca","Latitud":	4.9488030165	,"Longitud":	-73.9576589316	,"Altitud":	2605	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/368146957/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/208091819"},
	{"Tipo":"Mamifero","Nombre_Comun":"Comadreja Cola Larga","Nombre_Cientifico":"Neogale frenata","Habitat":"Boavita, Boyaca","Latitud":	6.334741484	,"Longitud":	-72.5857063383	,"Altitud":	2167	,"imagen":"https://static.inaturalist.org/photos/256273869/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/148781286"},
	{"Tipo":"Mamifero","Nombre_Comun":"Venado de Cola Blanca","Nombre_Cientifico":"Odocoileus virginianus","Habitat":"Embalse de Chuza, Fomeque, Cundinamarca","Latitud":	4.6133489964	,"Longitud":	-73.7128673891	,"Altitud":	2990	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/354444076/original.jpg","direccion_web":"https://colombia.inaturalist.org/observations/200853365"},
	{"Tipo":"Plantas","Nombre_Comun":"Esterilla","Nombre_Cientifico":"Orthrosanthus chimboracensis","Habitat":"Rondon, Boyaca","Latitud":	5.456073269	,"Longitud":	-73.1830275804	,"Altitud":	2546	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/392900892/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221841671"},
	{"Tipo":"Plantas","Nombre_Comun":"Curubo","Nombre_Cientifico":"Passiflora adulterina","Habitat":"Toca, Boyaca","Latitud":	5.5967028934	,"Longitud":	-73.1213223562	,"Altitud":	2810	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/392942597/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221864292"},
	{"Tipo":"Reptil","Nombre_Comun":"Pajarera de Shropshire","Nombre_Cientifico":"Phrynonax shropshirei","Habitat":"Caparrapi, Cundinamarca","Latitud":	5.4835448557	,"Longitud":	-74.5349447429	,"Altitud":	165	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/355833664/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/201563926"},
	{"Tipo":"Ave","Nombre_Comun":"Titiribi Pechirrojo","Nombre_Cientifico":"Pyrocephalus rubinus","Habitat":"Suba, Bogota, Cundinamarca","Latitud":	4.7202039656,	"Longitud":	 -74.0978201616	,"Altitud":	2625	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/392965263/original.jpg","direccion_web":"https://colombia.inaturalist.org/observations/221877734"},
	{"Tipo":"Ave","Nombre_Comun":"Tordo Llanero","Nombre_Cientifico":"Quiscalus lugubris","Habitat":"Cucaita, Boyaca","Latitud":	5.5441936607	,"Longitud":	-73.4541828185	,"Altitud":	2650	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/390892803/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/220764938"},
	{"Tipo":"Anfibio","Nombre_Comun":"Sapo del Obispo","Nombre_Cientifico":"Rhinella alata","Habitat":"Colegio La Magola, Supat, Cundinamarca","Latitud":	5.0337506762	,"Longitud":	-74.2719054359	,"Altitud":	1780	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/385143230/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/217698171"},
	{"Tipo":"Anfibio","Nombre_Comun":"Sapo Gigante","Nombre_Cientifico":"Rhinella marina","Habitat":"Chipaque, Cundinamarca","Latitud":	4.4338785401	,"Longitud":	-74.0137063712	,"Altitud":	2400	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/347213672/original.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/197177219"},
	{"Tipo":"Mamifero","Nombre_Comun":"Ardilla Andina","Nombre_Cientifico":"Sciurus pucheranii","Habitat":"La Maquina, Pacho, Cundinamarca","Latitud":	5.1382602695	,"Longitud":	-74.1938683252	,"Altitud":	2136	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/384355558/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/217274230"},
	{"Tipo":"Ave","Nombre_Comun":"Chipe Garganta Naranja","Nombre_Cientifico":"Setophaga fusca","Habitat":"Villa de Leyva, Boyaca","Latitud":	5.6359154767	,"Longitud":	-73.5270365449	,"Altitud":	2149	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/363522581/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/205581020"},
	{"Tipo":"Ave","Nombre_Comun":"Jilguero Andino","Nombre_Cientifico":"Spinus spinescens","Habitat":"La Calera, Cundinamarca","Latitud":	4.6722410285	,"Longitud":	-73.9589064941	,"Altitud":	2718	,"imagen":"https://static.inaturalist.org/photos/390103919/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/220343177"},
	{"Tipo":"Reptil","Nombre_Comun":"Lagarto Collarejo","Nombre_Cientifico":"Stenocercus trachycephalus","Habitat":"Moniquira, Boyaca","Latitud":	5.8006354964	,"Longitud":	-73.5472397134	,"Altitud":	1669	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/388656870/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/219572176"},
	{"Tipo":"Mamifero","Nombre_Comun":"Tamandua ","Nombre_Cientifico":"Tamandua mexicana","Habitat":"Puerto Boyaca, Boyaca","Latitud":	6.0573215394	,"Longitud":	-74.5234990611	,"Altitud":	145	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/353826808/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/200534183"},
	{"Tipo":"Insecto","Nombre_Comun":"Abejitas del Sudor","Nombre_Cientifico":"Tribu Halictini","Habitat":"Duitama, Boyaca","Latitud":	5.8273192806	,"Longitud":	-73.0426333845	,"Altitud":	2590	,"imagen":"https://static.inaturalist.org/photos/388553795/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/219514899"},
	{"Tipo":"Ave","Nombre_Comun":"Mirla Patinaranja","Nombre_Cientifico":"Turdus fuscater","Habitat":"Mosquera, Cundinamarca","Latitud":	4.7099966	,"Longitud":	-74.2260384	,"Altitud":	2516	,"imagen":"https://static.inaturalist.org/photos/390117084/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/220351995"},
	{"Tipo":"Mamifero","Nombre_Comun":"Zorra Gris","Nombre_Cientifico":"Urocyon cinereoargenteus","Habitat":"Nevado del cocuy, Boyaca","Latitud":	6.4941667311	,"Longitud":	-72.2975002974	,"Altitud":	5380	,"imagen":"https://static.inaturalist.org/photos/279900627/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/161908876"},
	{"Tipo":"Insecto","Nombre_Comun":"Polillas","Nombre_Cientifico":"Xanthyris flaveolata","Habitat":"Santa Maria, Boyaca","Latitud":	4.8801781165	,"Longitud":	-73.2946005249	,"Altitud":	850	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/384679556/large.jpg","direccion_web":"https://colombia.inaturalist.org/observations/217443558"},
	{"Tipo":"Ave","Nombre_Comun":"Mosquerito Caridorado","Nombre_Cientifico":"Zimmerius chrysops","Habitat":"Garagoa, Boyaca","Latitud":	5.0934982217	,"Longitud":	-73.3159367248	,"Altitud":	1650	,"imagen":"https://inaturalist-open-data.s3.amazonaws.com/photos/392862939/large.jpeg","direccion_web":"https://colombia.inaturalist.org/observations/221822606"}	]

# Crear DataFrame
df = pd.DataFrame(cadenajson)

# Agregar columna para el departamento
df['Departamento'] = df['Habitat'].apply(lambda x: 'Boyacá' if 'Boyaca' in x else 'Cundinamarca')

# Filtrar datos por departamento
boyaca_data = df[df['Departamento'] == 'Boyacá']
cundinamarca_data = df[df['Departamento'] == 'Cundinamarca']

# Crear un mapa de colores para cada tipo de organismo
colores = {
    'Plantas': 'green',
    'Mamifero': 'brown',
    'Reptil': 'orange',
    'Ave': 'blue',
    'Insecto': 'red',
    'Anfibio': 'purple'
}

# Crear gráficos para Boyacá
plt.figure(figsize=(10, 6))
for tipo in boyaca_data['Tipo'].unique():
    subset = boyaca_data[boyaca_data['Tipo'] == tipo]
    plt.scatter(subset['Longitud'], subset['Latitud'], c=colores[tipo], label=tipo)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Observaciones en Boyacá')
plt.legend()
plt.savefig("Observaciones en Boyaca")
plt.show()

# Crear gráficos para Cundinamarca
plt.figure(figsize=(10, 6))
for tipo in cundinamarca_data['Tipo'].unique():
    subset = cundinamarca_data[cundinamarca_data['Tipo'] == tipo]
    plt.scatter(subset['Longitud'], subset['Latitud'], c=colores[tipo], label=tipo)
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Observaciones en Cundinamarca')
plt.legend()
plt.savefig("Observaciones en cundinamarca")
plt.show()