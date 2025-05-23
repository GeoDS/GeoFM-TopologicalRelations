from collections import defaultdict
import openai
import csv

import sys

if len(sys.argv) < 2:
    print("Usage: python script.py filename")
    sys.exit(1)

filename = sys.argv[1]
# filename = "3_answer_object_place_type_3.csv"
headers = ["relation_predicate", "subject_place_name","object_place_name", "Response","actual_relation"]

client = openai.OpenAI(api_key='')
def run(place_name_subject,place_name_object,relation_predicate,relation):
    response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": """
                    The given seven PREDICATES: contains, is within, touches, crosses, disjoint, overlaps, equals. 
                    Given a sentence that include a vernacular spatial relation term: please give the corresponding PREDICATES. 
                    - Indicate spatial relation from A to B only.
                    - The vernacular spatial relation term should consider its typical meanings of the terms and the general geographical relationship it represent. Also pay attention to any other context that you can get from the sentence. 
                    - MAKE SURE the [PREDICATE] satisfies the the dimension requirements defined by DE-9IM and OGC given Geometry Type A and Geometry Type B.
                    - MAKE SURE that the output includes all plausible predicates and excludes any that are impossible or irrelevant in the given context. 
                    OUTPUT FORMAT: 
                        Analysis: Provide a detailed, professional, and coherent examination of the spatial relation from A to B.
                        Answer: A [PREDICATE1/PREDICATE2...] B. For example: A [overlaps/is within] B
"""},
                {"role": "user", "content": """given the sentence: A {} B and A is {}, and B is {}.""".format(relation_predicate,place_name_subject,place_name_object)}
            ],
            temperature=0.1
    )
    # with open("3_answer_object_place_type_2.txt","a") as outputfile:
    #     line="""relation_predicate:{},object_place_type:{}, response:{}""".format(relation_predicate,place_name_object,response.choices[0].message.content)
    #     outputfile.writelines(line)
    #     outputfile.writelines("\n")
    line = [relation_predicate, place_name_subject, place_name_object, response.choices[0].message.content,relation]
    with open(filename, "a", newline="") as outputfile: 
        csvwriter = csv.writer(outputfile)
        if outputfile.tell() == 0:
            csvwriter.writerow(headers)
        csvwriter.writerow(line)


# descrption_list=[["between","Cotati in California","Petaluma in California"],
# ["between","Pacifica in California","San Francisco in California"],
# ["between","Pacifica in California","Half Moon Bay in California"],
# ["between","Beaumont in Texas","Lumberton in Texas"],
# ["between","Rosenberg in Texas","Sealy in Texas"],
# ["between","Palestine in Texas","Rusk in Texas"],
# ["between","Corpus Christi in Texas","Harlingen in Texas"],
# ["between","Weimar in Texas","San Antonio/Austin/Houston in Texas"],
# ["between","Belton in Texas","Waco in Texas"],
# ["between","Belton in Texas","Austin in Texas"],
# ["between","Grapevine in Texas","Dallas in Texas"],
# ["between","Grapevine in Texas","Fort Worth in Texas"],
# ["between","Orchard in Texas","Rosenberg in Texas"],
# ["between","Orchard in Texas","Wallis in Texas"],
# ["between","Cotati in California","Rohnert Par in California"],
# ["between","Palm Springs in California","Rancho Mirage in California"],
# ["between","Monterey in California","Santa Cruz in California"],
# ["between","Rancho Mirage in California"," Cathedral City in California"],
# ["between","Emeryville in California","Berkeley in California"],
# ["between","Emeryville in California","Oakland in California"],
# ["between","Grand Terrace in California","Colton in California"],
# ["between","Grand Terrace in California","Highgrove in California"],
# ["between","La Quinta in California","Indian Wells in California"],
# ["between","La Quinta in California","Indio in California"],
# ["between","Rancho Mirage in California","Palm Springs in California"],
# ["between","Rancho Mirage in California","Palm Desert in California"],
# ["between","Cotati in California","Rohnert Park in California"],
# ["between","San Bruno in California","South San Francisco in California"],
# ["between","San Bruno in California","Millbrae in California"],
# ["between","Indian Wells in California","Palm Desert in California"],
# ["between","Indian Wells in California","La Quinta in California"],
# ["suburb of","The Colony in Texas","Dallas in Texas"],
# ["suburb of","Robstown in Texas","Corpus Christi in Texas"],
# ["suburb of","Burleson in Texas","Fort Worth in Texas"],
# ["suburb of","The Hills in Texas","Austin in Texas"],
# ["suburb of","Argyle in Texas","Fort Worth in Texas"],
# ["suburb of","Justin in Texas","Fort Worth in Texas"],
# ["suburb of","Southlake in Texas","Dallas/Fort Worth in Texas"],
# ["suburb of","Bedford in Texas","Dallas in Texas"],
# ["suburb of","Bedford in Texas","Fort Worth in Texas"],
# ["suburb of","Colleyville in Texas","Dallas in Texas"],
# ["suburb of","Colleyville in Texas","Fort Worth in Texas"],
# ["suburb of","Grapevine in Texas","Dallas in Texas"],
# ["suburb of","Grapevine in Texas","Fort Worth in Texas"],
# ["suburb of","Early in Texas","Brownwood in Texas"],
# ["suburb of","Sun Prairie in Wisconsin","madison in Wisconsin"],
# ["suburb of","Fitchburg in Wisconsin","madison in Wisconsin"],
# ["suburb of","Glendale in Wisconsin","milwaukee city in Wisconsin"],
# ["suburb of","Middleton in Wisconsin","madison in Wisconsin"],
# ["suburb of","Monona in Wisconsin","madison in Wisconsin"],
# ["suburb of","West Allis in Wisconsin","milwaukee in Wisconsin"],
# ["suburb of","White Settlement in Texas","Fort Worth in Texas"],
# ["suburb of","Haltom City in Texas","Fort Worth in Texas"],
# ["suburb of","Richardson in Texas","Dallas in Texas"],
# ["suburb of","Saginaw in Texas","Fort Worth in Texas"],
# ["suburb of","Coppell in Texas","Dallas in Texas"],
# ["suburb of","Dalworthington Gardens in Texas","Arlington in Texas"],
# ["suburb of","Forest Hill in Texas","Fort Worth in Texas"],
# ["suburb of","Portland in Texas","Corpus Christi in Texas"],
# ["suburb of","Pflugerville in Texas","Austin in Texas"],
# ["suburb of","Cedar Park in Texas","Austin in Texas"],
# ["suburb of","Wake Village in Texas","Texarkana in Texas"],
# ["suburb of","Watauga in Texas","Fort Worth in Texas"],
# ["suburb of","West Lake Hills in Texas","Austin in Texas"],
# ["suburb of","Farmers Branch in Texas","Dallas in Texas"],
# ["suburb of","Nash in Texas","Texarkana in Texas"],
# ["suburb of","Irving in Texas","Dallas in Texas"],
# ["straddle","Stoughton in Wisconsin","yahara river in Wisconsin"],
# ["straddle","Wisconsin Dells in Wisconsin","adams in Wisconsin"],
# ["straddle","Wisconsin Dells in Wisconsin","columbia in Wisconsin"],
# ["straddle","Wisconsin Dells in Wisconsin","juneau in Wisconsin"],
# ["straddle","Wisconsin Dells in Wisconsin","sauk in Wisconsin"],
# ["along","Mondovi in Wisconsin","Buffalo River in Wisconsin"],
# ["along","Omro in Wisconsin","fox river in Wisconsin"],
# ["along","Ukiah in California","Route 101, United State"],
# ["along","Ceres in California","State Route 99"],
# ["along","Luling in Texas","San Marcos River in Texas"],
# ["along","Orchard in Texas","State Highway 36 (SH 36) in Texas"],
# ["along","Brazos Bend in Texas","Brazos River in Texas"],
# ["along","South Lake Tahoe in California","Lake Tahoe in California"],
# ["along","Two Rivers in Wisconsin","Lake Michigan"],
# ["near","Santa Fe Dam Recreation Area in California","San Gabriel River in California"],
# ["near","Baraboo in Wisconsin","devil's lake state park in Wisconsin"],
# ["near","Whitewater in Wisconsin","kettle moraine state forest in Wisconsin"],
# ["near","Smithville in Texas","Colorado River in Texas"],
# ["near","La Grange in Texas","Colorado River in Texas"],
# ["near","Surfside Beach in Texas","Freeport in Texas"],
# ["near","Goleta in California","University of California, Santa Barbara in California"],
# ["near","Lompoc in California","Vandenberg Space Force Base in California"],
# ["near","Converse in Texas","Randolph Air Force Base in Texas"],
# ["near","Lakewood Village in Texas","Lewisville Lake in Texas"],
# ["near","Lynwood in California","Compton in California"],
# ["near","Lynwood in California","South Gate in California"],
# ["near","Oconomowoc in Wisconsin","oconomowoc lake  in Wisconsin"],
# ["near","Temple in Texas","Belton in Texas"],
# ["situated on","Kaukauna in Wisconsin","fox river in Wisconsin"],
# ["situated on","Neenah in Wisconsin","fox river in Wisconsin"],
# ["situated on","Palos Verdes Estates in California","Palos Verdes Peninsula in California"],
# ["situated on","Lake Geneva in Wisconsin","geneva lake in Wisconsin"],
# ["situated on","Neenah in Wisconsin","little lake butte des morts in Wisconsin"],
# ["situated on","Neenah in Wisconsin","lake winnebago in Wisconsin"],
# ["on the shore of","Lake Elsinore","Lake Elsinore"],
# ["on the shore of","Racine in Wisconsin","lake michigan"],
# ["on the shore of","Albany in California","San Francisco Bay in California"],
# ["on the shore of","Clear Lake in California","Lakeport in California"],
# ["on the shore of","San Pablo Bay in California","Vallejo in California"],
# ["on the shore of","Carquinez Strait in California","Martinez in California"],
# ["located on","Weimar in Texas","Interstate 10"],
# ["located on","Weimar in Texas","US 90"],
# ["located on","Madison in Wisconsin","lake mendota in Wisconsin"],
# ["located on","West Tawakoni in Texas","Lake Tawakoni in Texas"],
# ["located on","Lago Vista in Texas","Lake Travis in Texas"],
# ["located on","Robert Lee in Texas","the Colorado River in Texas"],
# ["located on","Wharton in Texas","Colorado River in Texas"],
# ["located on","Orange","Sabine River"],
# ["located on","Helotes in Texas","San Antonio in Texas"],
# ["located on","Dyess Air Force Base in Texas","Abilene in Texas"],
# ["to the direction","Seal Beach in California","Long Beach in California"],
# ["to the direction","racine in Wisconsin","Kenosha in Wisconsin"],
# ["to the direction","Tomahawk in Wisconsin","town of tomahawk  in Wisconsin"],
# ["to the direction","Millbrae in California","San Andreas Lake in California"],
# ["to the direction","Guadalupe in California","Santa Maria in California"],
# ["to the direction","Merced in California","Yosemite National Park in California"],
# ["to the direction","Yosemite National Park in California","Kings Canyon National Park in California"],
# ["to the direction","santa barbara in California","San Francisco in California"],
# ["to the direction","Palo Alto in California","Stanford University in California"],
# ["to the direction","San Jacinto  in California","Hemet in California"],
# ["to the direction","San Leandro,california","Oakland in California"],
# ["to the direction","West Covina in California","Covina in California"],
# ["to the direction","West Covina in California","Baldwin Park in California"],
# ["to the direction","Garden Grove in California","Westminster in California"],
# ["to the direction","Temecula in California","Murrieta in California"],
# ["to the direction","West Covina in California","Walnut in California"],
# ["to the direction","West Covina in California","La Puente in California"],
# ["to the direction","West Covina in California","Valinda in California"],
# ["to the direction","Merrill in Wisconsin","town of merrill in Wisconsin"],
# ["to the direction","Topanga in California","Malibu in California"],
# ["to the direction","West Covina in California","Irwindale in California"],
# ["to the direction","Alameda County in California","Stanislaus County in California"],
# ["to the direction","San Dimas in California","Covina in California"],
# ["to the direction","San Dimas in California","Glendora in California"],
# ["to the direction","Norco in California","Riverside in California"],
# ["home to","Hemet in California","Hemet Valley Medical Center in California"],
# ["home to","Kenosha in Wisconsin","gateway technical college  in Wisconsin"],
# ["home to","Appleton in Wisconsin","fox cities exhibition center in Wisconsin"],
# ["home to","Appleton in Wisconsin","fox cities performing arts center in Wisconsin"],
# ["home to","Appleton in Wisconsin","lawrence university in Wisconsin"],
# ["home to","Kenosha in Wisconsin","carthage college in Wisconsin"],
# ["home to","La Crosse in Wisconsin","university of wisconsin-la crosse in Wisconsin"],
# ["home to","La Crosse in Wisconsin","western technical college  in Wisconsin"],
# ["home to","Madison in Wisconsin","overture center for the arts in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","marquette university in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","msoe in Wisconsin"],
# ["home to","River Falls in Wisconsin","university of wisconsin‚Äìriver falls  in Wisconsin"],
# ["home to","Stevens Point in Wisconsin","mid-state technical college  in Wisconsin"],
# ["home to","Whitewater in Wisconsin","university of wisconsin‚whitewater  in Wisconsin"],
# ["home to","Kenosha in Wisconsin","jockey international in Wisconsin"],
# ["home to","Madison in Wisconsin","exact sciences in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","headquarters of harley-davidson"],
# ["home to","Madison in Wisconsin","university research park  in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","northwestern mutual in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","wec energy group in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","rockwell automation in Wisconsin"],
# ["home to","Chippewa Falls in Wisconsin","irvine park in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","brewers in Wisconsin"],
# ["home to","Baraboo in Wisconsin","circus world museum in Wisconsin"],
# ["home to","Madison in Wisconsin","henry vilas zoo in Wisconsin"],
# ["home to","Milwaukee in Wisconsin","discovery world in Wisconsin"],
# ["home to","Stevens Point in Wisconsin","university of wisconsin‚Äìstevens point in Wisconsin"],
# ["home to","Austin in Texas","University of Texas at Austin in Texas"],
# ["home to","San Antonio in Texas","South Texas Medical Center in Texas"],
# ["home to","Houston in Texas","Texas Medical Center in Texas"],
# ["home to","Lubbock in Texas","Texas Tech University in Texas"],
# ["home to","Willow Park in Texas","Squaw Creek golf course in Texas"],
# ["home to","Dumas in Texas","Moore County Airport in Texas"],
# ["home to","Eau Claire in Wisconsin","Menards distribution center in Wisconsin"],
# ["home to","Delavan in Wisconsin","delavan lake in Wisconsin"],
# ["home to","San Marcos in Texas","Texas State University in Texas"],
# ["just direction of","New Braunfels,texas","San Antonio,texas"],
# ["just direction of","Salinas in California","San Francisco Bay California"],
# ["just direction of","Garden Grove in California","Disneyland in California"],
# ["just direction of","Farmersville in California","Visalia in California"],
# ["just direction of","Leander,texas","Austin,texas"],
# ["just direction of","Hawkins,texas","Jarvis Christian College,texas"],
# ["just direction of","Del Rey Oaks in California","Seaside in California"],
# ["just direction of","Menifee in California","Murrieta in California"],
# ["just direction of","Montebello in California","East Los Angeles in California"],
# ["just direction of","West lake hills,travis county in Texas","Austin,texas"],
# ["just direction of","Benicia in California","Vallejo in California"],
# ["mostly in","Columbus in Wisconsin","columbia in Wisconsin"],
# ["mostly in","Menasha in Wisconsin","winnebago county in Wisconsin"],
# ["mostly in","Eau Claire in Wisconsin","eau claire county in Wisconsin"],
# ["mostly in","Berlin in Wisconsin","town of berlin in Wisconsin"],
# ["mostly in","Medford in Wisconsin","town of medford  in Wisconsin"],
# ["mostly in","Mondovi in Wisconsin","town of mondovi in Wisconsin"],
# ["mostly in","Weyauwega in Wisconsin","town of weyauwega in Wisconsin"],
# ["partly in","Columbus in Wisconsin","dodge in Wisconsin"],
# ["partly in","Eau Claire in Wisconsin","chippewa county in Wisconsin"],
# ["partly in","Menasha in Wisconsin","doty island in Wisconsin"],
# ["partly in","Cuba City in Wisconsin","lafayette county in Wisconsin"],
# ["partly in","Cumberland in Wisconsin","town of cumberland  in Wisconsin"],
# ["partly in","Chilton in Wisconsin","town of chilton  in Wisconsin"],
# ["partly in","Delavan in Wisconsin","town of delavan in Wisconsin"],
# ["partly in","Lake Mills in Wisconsin","town of lake mills  in Wisconsin"],
# ["partly in","Thorp in Wisconsin","town of thorp in Wisconsin"],
# ["partly in","Thorp in Wisconsin","town of withee  in Wisconsin"],
# ["partly in","Columbus in Wisconsin","elba  in Wisconsin"],
# ["partly in","Mondovi in Wisconsin","town of naples  in Wisconsin"],
# ["within","Universal Studios Hollywood in California","Universal City in California"],
# ["within","Pearland in Texas","Brazoria County in Texas"],
# ["within","Garland in Texas","Dallas County in Texas"],
# ["within","Brillion in Wisconsin","town of brillion  in Wisconsin"],
# ["within","Fox Lake in Wisconsin","town of fox lake  in Wisconsin"],
# ["within","Loyal in Wisconsin","town of loyal in Wisconsin"],
# ["within","Mineral in Wisconsin","town of mineral point in Wisconsin"],
# ["within","New Holstein in Wisconsin","town of new holstein  in Wisconsin"],
# ["within","Peshtigo in Wisconsin","town of peshtigo in Wisconsin"],
# ["within","Princeton in Wisconsin","town of princeton in Wisconsin"],
# ["within","Seymour in Wisconsin","town of osborn  in Wisconsin"],
# ["within","Seymour in Wisconsin","town of seymour in Wisconsin"],
# ["within","Verona in Wisconsin","town of verona in Wisconsin"],
# ["within","California State University Long Beach in California","Long Beach in California"],
# ["surrounds","Richmond in California","San Pablo in California"],
# ["surrounds","Fort Jones", "Mount Shasta"],
# ["surrounds","Mequon in Wisconsin","Thiensville in Wisconsin"],
# ["surrounds","Hayward in California","Union City in California"],
# ["surrounds","Haltom City in Texas","Fort Worth in Texas"],
# ["surrounds","Haltom City in Texas","North Richland Hills in Texas"],
# ["surrounds","Haltom City in Texas","Watauga in Texas"],
# ["surrounds","Haltom City in Texas","Richland Hills in Texas"],
# ["surrounds","Bellaire in Texas","West University Place in Texas"],
# ["surrounds","Hurst in Texas","Euless in Texas"],
# ["surrounds","Hurst in Texas","Grapevine in Texas"],
# ["surrounds","Tomah in Wisconsin","town of la grange  in Wisconsin"],
# ["surrounds","Piedmont in California","Oakland in California"],
# ["surrounds","Cockrell Hill in Texas","Dallas in Texas"],
# ["surrounds","Artesia in California","Cerritos in California"],
# ["surrounds","Newark in California","Fremont in California"],
# ["surrounds","Signal Hill in California","Long Beach in California"],
# ["surrounds","Los Angeles in California","West Hollywood in California"],
# ["surrounds","Eastvale in California","Chino in California"],
# ["surrounds","Eastvale in California","Ontario in California"],
# ["surrounds","Eastvale in California","Jurupa Valley in California"],
# ["surrounds","Eastvale in California","Norco in California"],
# ["surrounds","Eastvale in California","Corona in California"],
# ["surrounds","Darlington in Wisconsin","town of darlington  in Wisconsin"],
# ["surrounds","Hayward in Wisconsin","town of hayward  in Wisconsin"],
# ["surrounds","Peshtigo in Wisconsin","town of peshtigo in Wisconsin"],
# ["surrounds","Reedsburg in Wisconsin","town of reedsburg in Wisconsin"],
# ["surrounds","Ripon in Wisconsin","town of ripon in Wisconsin"],
# ["surrounds","Tomah in Wisconsin","town of tomah in Wisconsin"],
# ["surrounds","Pewaukee in Wisconsin","village of pewaukee  in Wisconsin"],
# ["surrounds","Hurst in Texas","Bedford in Texas"],
# ["surrounds","Hurst in Texas","Fort Worth in Texas"],
# ["surrounds","Hurst in Texas","Richland Hills in Texas"],
# ["surrounds","Hurst in Texas","North Richland Hills in Texas"],
# ["surrounds","Hurst in Texas","Colleyville in Texas"],
# ["surrounds","Beverly Hills in Texas","Waco in Texas"],
# ["surrounds","Leon Valley in Texas","San Antonio in Texas"],
# ["surrounds","Bellaire in Texas","Houston in Texas"],
# ["surrounds","West University Place in Texas","Houston in Texas"],
# ["surrounds","West University Place in Texas","Southside Place in Texas"],
# ["surrounds","Alamo Heights in Texas","San Antonio in Texas"],
# ["surrounds","Sunset Valley in Texas","Austin in Texas"],
# ["surrounds","Sand City in California","Seaside in California"]]

descrption_list=[
['borders','touches','place_name','Universal City, Texas/San Antonio, Texas'],
['borders','touches','place_name','Laguna Niguel, California/Laguna Hills, California'],
['borders','touches','place_name','Berkeley, California/Oakland, California'],
['borders','touches','place_name','San Mateo, California/Burlingame, California'],
['borders','touches','place_name','Farwell, Texas/Texico, New Mexico'],
['connect C and','crosses','place_name','State Route 52/Santee,California'],
['connect C and','crosses','place_name','interstate 94,wisconsin/Chicago'],
['connect C and','crosses','place_name','State Route 17/San Jose, California'],
['connect C and','crosses','place_name','Rainbow Bridge, Texas/Port Arthury, Texas'],
['connect C and','crosses','place_name','State Route 86/Brawley'],
['extend into','overlaps','place_name','San Marcos, Texas/Caldwell County, Texas'],
['extend into','overlaps','place_name','Royse City, Texas/Collin county, Texas'],
['extend into','overlaps','place_name','Seagoville, Texas/Kaufman County, Texas'],
['extend into','overlaps','place_name','Royse City, Texas/Hunt county, Texas'],
['extend into','overlaps','place_name','Longview, Texas/Harrison County, Texas'],
['has part of the population in','overlaps','place_name','Stanley,wisconsin/chippewa county,wisconsin'],
['has part of the population in','overlaps','place_name','Marshfield,wisconsin/marathon county,wisconsin'],
['has part of the population in','overlaps','place_name','Abbotsford,wisconsin/marathon county ,wisconsin'],
['has part of the population in','overlaps','place_name','Edgerton,wisconsin/dane county,wisconsin'],
['has part of the population in','overlaps','place_name','New London,wisconsin/outagamie county,wisconsin'],
['includes','contains','place_name','Monterey,california/Monterey Bay Aquarium,california'],
['includes','contains','place_name','Riverside,california/ California Museum of Photography,california'],
['includes','contains','place_name','Riverside,california/Museum of Riverside,california'],
['includes','contains','place_name','Superior,wisconsin/billings park,wisconsin'],
['includes','contains','place_name','Lakewood,california/Bellflower,lakewood,california'],
['is adjacent to','touches','place_name','Lake Worth, Texas/Lake Worth, Texas'],
['is adjacent to','touches','place_name','Crandon,wisconsin/Town of Crandon,wisconsin'],
['is adjacent to','touches','place_name','River Falls,wisconsin/kinnickinnic,wisconsin'],
['is adjacent to','touches','place_name','Rancho Mirage, California/Cathedral City, California'],
['is adjacent to','touches','place_name','Shullsburg,wisconsin/town of shullsburg,wisconsin'],
['is along','crosses','place_name','Ukiah, California/Route 101, United State'],
['is along','crosses','place_name','Omro,wisconsin/fox river,wisconsin'],
['is along','crosses','place_name','Brazos Bend, Texas/Brazos River, Texas'],
['is along','crosses','place_name','Orchard, Texas/State Highway 36 (SH 36), Texas'],
['is along','crosses','place_name','Mondovi,wisconsin/Buffalo River,wisconsin'],
['is an enclave of','touches','place_name','University Park, Texas/Dallas, Texas'],
['is an enclave of','touches','place_name','Balcones Heights, Texas/San Antonio, Texas'],
['is an enclave of','touches','place_name','Leon Valley,texas/San Antonio,texas'],
['is an enclave of','touches','place_name','Kirby, Texas/San Antonio, Texas'],
['is an enclave of','touches','place_name','Lake San Marcos, California/San Marcos, California'],
['is between C and','disjoint','place_name','Orchard, Texas/Wallis, Texas'],
['is between C and','disjoint','place_name','Weimar, Texas/San Antonio/Austin/Houston, Texas'],
['is between C and','disjoint','place_name','Cotati, California/Petaluma, California'],
['is between C and','disjoint','place_name','Palestine, Texas/Rusk, Texas'],
['is between C and','disjoint','place_name','Rosenberg, Texas/Sealy, Texas'],
['is between C and','touches','place_name','San Bruno, California/Millbrae, California'],
['is between C and','touches','place_name','Rancho Mirage, California/ Cathedral City, California'],
['is between C and','touches','place_name','South Pasadena, California/Pasadena, California'],
['is between C and','touches','place_name','Grand Terrace, California/Colton, California'],
['is between C and','touches','place_name','Indian Wells, California/La Quinta, California'],
['is bordered by','disjoint','place_name','the Pacific Ocean, California/Huntington Beach, California'],
['is bordered by','disjoint','place_name','Huntington Park, California/Commerce, California'],
['is bordered by','disjoint','place_name','Maywood, California/Commerce, California'],
['is bordered by','disjoint','place_name','Beaumont, California/San Jacinto, California'],
['is bordered by','disjoint','place_name','Newport Beach, California/Huntington Beach, California'],
['is bordered by','touches','place_name','Glendora, California/Covina, California'],
['is bordered by','touches','place_name','Long Beach, California/Bellflower, California'],
['is bordered by','touches','place_name','San Marcos, California/Carlsbad, California'],
['is bordered by','touches','place_name','Glendora, California/San Dimas, California'],
['is bordered by','touches','place_name','South Houston, Texas/Pasadena, Texas'],
['is bounded by','touches','place_name','Stanton, California/Garden Grove, California'],
['is bounded by','touches','place_name','Malibu, california/Topanga, california'],
['is bounded by','touches','place_name','Azusa, California/Duarte, California'],
['is bounded by','touches','place_name','Irwindale, California/Duarte, California'],
['is bounded by','touches','place_name','Stanton, California/Anaheim, California'],
['is halfway between C and','disjoint','place_name','Belmont, California/San Jose, California'],
['is halfway between C and','disjoint','place_name','Waco, Texas/Dallas, Texas'],
['is halfway between C and','disjoint','place_name','East Palo Alto,california/San Jose, California'],
['is halfway between C and','disjoint','place_name','Kenosha,wisconsin/Chicago,Illinois'],
['is halfway between C and','disjoint','place_name','Kenosha,wisconsin/Milwaukee,wisconsin'],
['is home to','contains','place_name','Milwaukee,wisconsin/rockwell automation,wisconsin'],
['is home to','contains','place_name','La Crosse,wisconsin/university of wisconsin-la crosse,wisconsin'],
['is home to','contains','place_name','Baraboo,wisconsin/circus world museum,wisconsin'],
['is home to','contains','place_name','Milwaukee,wisconsin/headquarters of harley-davidson'],
['is home to','contains','place_name','Austin, Texas/University of Texas at Austin, Texas'],
['is in','disjoint','place_name','Santa Clara County, California/california'],
['is in','disjoint','place_name','Long Beach, California/Southern California, California'],
['is in','disjoint','place_name','Dunsmuir, California/Northern California, California'],
['is in','disjoint','place_name','Oakland, California/East Bay region, California'],
['is in','disjoint','place_name','San Marino, California/Los Angeles area, California'],
['is in','overlaps','place_name','Marion,wisconsin/shawano,wisconsin'],
['is in','overlaps','place_name','Burlington,wisconsin/walworth  county,wisconsin'],
['is in','overlaps','place_name','Marion,wisconsin/waupaca ,wisconsin'],
['is in','overlaps','place_name','Palmdale, California/Antelope Valley, California'],
['is in','overlaps','place_name','Kiel,wisconsin/manitowoc county,wisconsin'],
['is in','within','place_name','Algoma,wisconsin/kewaunee county,wisconsin'],
['is in','within','place_name','Thorp,wisconsin/clark county,wisconsin'],
['is in','within','place_name','Arcadia,wisconsin/trempealeau county,wisconsin'],
['is in','within','place_name','Plymouth,wisconsin/sheboygan county,wisconsin'],
['is in','within','place_name','Mayville,wisconsin/dodge county,wisconsin'],
['is located in','disjoint','place_name','Dublin, Texas/none, Texas'],
['is located in','disjoint','place_name','Mount Pleasant, Texas/Northeast Texas'],
['is located in','disjoint','place_name','Patton Village, Texas/Greater Houston, Texas'],
['is located in','disjoint','place_name','Fremont, California/East Bay region, California'],
['is located in','disjoint','place_name','Retama Park, Texas/Selma, Texas'],
['is located in','within','place_name','Benbrook, Texas/Texas'],
['is located in','within','place_name','Hico, Texas/Hamilton County, Texas'],
['is located in','within','place_name','Tomahawk,wisconsin/lincoln county,wisconsin'],
['is located in','within','place_name','Whitewater,wisconsin/walworth county,wisconsin'],
['is located in','within','place_name','Rio Vista, California/Solano County, California'],
['is midway between C and','disjoint','place_name','Whitehall,wisconsin/eau claire ,wisconsin'],
['is midway between C and','disjoint','place_name','Whitehall,wisconsin/la crosse,wisconsin'],
['is midway between C and','disjoint','place_name','San Clemente, California/Los Angeles, California'],
['is midway between C and','disjoint','place_name','Midland,Midland County, Texas/Fort Worth, Texas'],
['is midway between C and','disjoint','place_name','San Clemente, California/San Diego, California'],
['is mostly in','overlaps','place_name','Columbus,wisconsin/columbia,wisconsin'],
['is mostly in','overlaps','place_name','Stafford,Texas/Fort Bend County,texas'],
['is mostly in','overlaps','place_name','Menasha,wisconsin/winnebago county,wisconsin'],
['is mostly in','overlaps','place_name','Eau Claire,wisconsin/eau claire county,wisconsin'],
['is mostly in','overlaps','place_name','O\'Donnell, Texas/Lynn County, Texas'],
['is near','disjoint','place_name','Dallas, Texas/Fort Worth, Texas'],
['is near','disjoint','place_name','Whitewater,wisconsin/kettle moraine state forest,wisconsin'],
['is near','disjoint','place_name','Stephenville, Texas/Dublin, Texas'],
['is near','disjoint','place_name','Laguna Niguel, California/Laguna Woods, California'],
['is near','disjoint','place_name','Houston, Texas/none, Texas'],
['is near','touches','place_name','Goleta, California/University of California, Santa Barbara, California'],
['is near','touches','place_name','Converse, Texas/Randolph Air Force Base, Texas'],
['is near','touches','place_name','Surfside Beach, Texas/Freeport, Texas'],
['is near','touches','place_name','Temple, Texas/Belton, Texas'],
['is near','touches','place_name','Lakewood Village, Texas/Lewisville Lake, Texas'],
['is neighboring','touches','place_name','Haltom City,texas/Fort Worth, Texas'],
['is neighboring','touches','place_name','Benicia, California/Vallejo, California'],
['is neighboring','touches','place_name','Haltom City,texas/North Richland Hills,texas'],
['is neighboring','touches','place_name','Los Alamitos, California/Cypress, California'],
['is neighboring','touches','place_name','Haltom City,texas/Watauga,texas'],
['is on','crosses','place_name','the city, Texas/Texas State Highway 31, Texas'],
['is on','crosses','place_name','Stamford, Texas/US Highway 277 and State Highway 6, Texas'],
['is on','crosses','place_name','Marina,California/State Route 1'],
['is on','crosses','place_name','Columbus,wisconsin/crawfish river,wisconsin'],
['is on','crosses','place_name','Stephenville, Texas/North Bosque River'],
['is part of','within','place_name','Schofield,wisconsin/Wausau Metropolitan Statistical Area(Marathon)'],
['is part of','within','place_name','Kaukauna,wisconsin/Appleton,Wisconsin Metropolitan Statistical Area(Calumet, Outagamie)'],
['is part of','within','place_name','Kenosha,wisconsin/Chicago metropolitan area(Wisconsin County: Kenosha, Illinois Counties: Cook, DeKalb, DuPage, Grundy, Kane, Kendall, Lake, McHenry, Will, Indiana Counties: Jasper, Lake, Newton, Porter)'],
['is part of','within','place_name','Stoughton,wisconsin/Madison Metropolitan Statistical Area(Columbia, Dane, Green, Iowa)'],
['is part of','within','place_name','Algoma,wisconsin/Green Bay Metropolitan Statistical Area(Brown, Kewaunee, Oconto)'],
['is partly in','overlaps','place_name','Friendswood, Texas/Galveston County, Texas'],
['is partly in','overlaps','place_name','Friendswood, Texas/Harris County, Texas'],
['is partly in','overlaps','place_name','Cumberland,wisconsin/town of cumberland ,wisconsin'],
['is partly in','overlaps','place_name','Cuba City,wisconsin/lafayette county,wisconsin'],
['is partly in','overlaps','place_name','Eau Claire,wisconsin/chippewa county,wisconsin'],
['is partly in','touches','place_name','Chilton,wisconsin/town of chilton ,wisconsin'],
['is partly in','touches','place_name','Thorp,wisconsin/town of thorp,wisconsin'],
['is partly in','touches','place_name','Chetek,wisconsin/town of chetek ,wisconsin'],
['is partly in','touches','place_name','Delavan,wisconsin/town of delavan,wisconsin'],
['is partly in','touches','place_name','Lake Mills,wisconsin/town of lake mills ,wisconsin'],
['is situated on','overlaps','place_name','Neenah,wisconsin/little lake butte des morts,wisconsin'],
['is situated on','overlaps','place_name','Lake Geneva,wisconsin/geneva lake,wisconsin'],
['is situated on','overlaps','place_name','Neenah,wisconsin/lake winnebago,wisconsin'],
['is situated on','overlaps','place_name','Palos Verdes Estates, California/Palos Verdes Peninsula, California'],
['is situated on','overlaps','place_name','Horseshoe Bay,texas/Lake Lyndon B. Johnson'],
['is suburb of','disjoint','place_name','Burleson, Texas/Fort Worth, Texas'],
['is suburb of','disjoint','place_name','Argyle, Texas/Fort Worth, Texas'],
['is suburb of','disjoint','place_name','The Colony, Texas/Dallas, Texas'],
['is suburb of','disjoint','place_name','Colleyville, Texas/Dallas, Texas'],
['is suburb of','disjoint','place_name','Southlake, Texas/Dallas/Fort Worth, Texas'],
['is suburb of','touches','place_name','Farmers Branch, Texas/Dallas, Texas'],
['is suburb of','touches','place_name','Forest Hill, Texas/Fort Worth, Texas'],
['is suburb of','touches','place_name','Sun Prairie,wisconsin/madison,wisconsin'],
['is suburb of','touches','place_name','Watauga, Texas/Fort Worth, Texas'],
['is suburb of','touches','place_name','Glendale,wisconsin/milwaukee city,wisconsin'],
['is surrounded by','touches','place_name','Newark, California/Fremont, California'],
['is surrounded by','touches','place_name','Hurst, Texas/Richland Hills, Texas'],
['is surrounded by','touches','place_name','Hayward, California/Union City, California'],
['is surrounded by','touches','place_name','Hurst, Texas/North Richland Hills, Texas'],
['is surrounded by','touches','place_name','Hurst, Texas/Fort Worth, Texas'],
['is the county seat of','within','place_name','Port Lavaca, Texas/Calhoun County, Texas'],
['is the county seat of','within','place_name','Corsicana, Texas/Navarro County, Texas'],
['is the county seat of','within','place_name','Waco, Texas/McLennan County, Texas'],
['is the county seat of','within','place_name','Madisonville, Texas/Madison County, Texas'],
['is the county seat of','within','place_name','Vega, Texas/Oldham County, Texas'],
['is the location of','contains','place_name','Fort Worth, Texas/Texas Christian University'],
['is the location of','contains','place_name','Fort Worth, Texas/ Texas A&M University School of Law'],
['is the location of','contains','place_name','St. Helena, california/Culinary Institute of America at Greystone'],
['is the location of','contains','place_name','Fort Worth, Texas/Fort Worth Museum of Science and History '],
['is the location of','contains','place_name','Fort Worth, Texas/Sid Richardson Museum'],
['is within','touches','place_name','Brillion,wisconsin/town of brillion ,wisconsin'],
['is within','touches','place_name','Loyal,wisconsin/town of loyal,wisconsin'],
['is within','touches','place_name','Verona,wisconsin/town of verona,wisconsin'],
['is within','touches','place_name','New Holstein,wisconsin/town of new holstein ,wisconsin'],
['is within','touches','place_name','Mineral,wisconsin/town of mineral point,wisconsin'],
['on the shore of','overlaps','place_name','Albany, California/San Francisco Bay, California'],
['on the shore of','overlaps','place_name','Racine,wisconsin/lake michigan'],
['on the shore of','overlaps','place_name','Clear Lake, California/Lakeport, California'],
['on the shore of','overlaps','place_name','San Pablo Bay, California/Vallejo, California'],
['on the shore of','overlaps','place_name','Carquinez Strait, California/Martinez, California'],
['share border with','touches','place_name','Walnut Creek, California/Concord,california'],
['share border with','touches','place_name','Rocklin,california/Lincoln, california'],
['share border with','touches','place_name','Walnut Creek, California/Lafayette, California'],
['share border with','touches','place_name','Culver City, California/Ladera Heights, California'],
['share border with','touches','place_name','Monte Sereno, California/Los Gatos, California'],
['surrounds','touches','place_name','Darlington,wisconsin/town of darlington ,wisconsin'],
['surrounds','touches','place_name','Hayward,wisconsin/town of hayward ,wisconsin'],
['surrounds','touches','place_name','Reedsburg,wisconsin/town of reedsburg,wisconsin'],
['surrounds','touches','place_name','Richmond, California/San Pablo, California'],
['surrounds','touches','place_name','Ripon,wisconsin/town of ripon,wisconsin']]

for description_word in descrption_list:
        relation_predicate = description_word[0]
        place_name_subject = description_word[3].split('/')[0]
        place_name_object = description_word[3].split('/')[1]
        relation=description_word[1]
        
        run(place_name_subject,place_name_object,relation_predicate,relation)
        print(relation_predicate,place_name_subject)


