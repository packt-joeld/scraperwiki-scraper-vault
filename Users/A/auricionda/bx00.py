import scraperwiki
import lxml.html
a=[
'http://www.bolivianexpress.org/blog/posts/altitude-adjustment',
'http://www.bolivianexpress.org/blog/posts/much-ado-about-potatoes',
'http://www.bolivianexpress.org/blog/posts/the-golden-grain-of-the-andes',
'http://www.bolivianexpress.org/blog/posts/life-as-a-trout',
'http://www.bolivianexpress.org/blog/posts/dawn-till-dusk-at-mercado-rodriguez',
'http://www.bolivianexpress.org/blog/posts/super-sweet-fifteen',
'http://www.bolivianexpress.org/blog/posts/why-didn-t-the-mcchicken-cross-the-road',
'http://www.bolivianexpress.org/blog/posts/eat-chew-love',
'http://www.bolivianexpress.org/blog/posts/food-reviews',
'http://www.bolivianexpress.org/blog/posts/gustu-a-new-flavour-in-town',
'http://www.bolivianexpress.org/blog/posts/editorial-reinventing-progress',
'http://www.bolivianexpress.org/blog/posts/tourism-and-sustainable-development-bolivia-looks-to-the-future',
'http://www.bolivianexpress.org/blog/posts/artful-rebellion',
'http://www.bolivianexpress.org/blog/posts/where-is-the-love',
'http://www.bolivianexpress.org/blog/posts/virtual-love-in-the-altiplano',
'http://www.bolivianexpress.org/blog/posts/how-to-love-life-itself',
'http://www.bolivianexpress.org/blog/posts/love-in-the-andes',
'http://www.bolivianexpress.org/blog/posts/amor-sin-pasion',
'http://www.bolivianexpress.org/blog/posts/a-healing-conundrum',
'http://www.bolivianexpress.org/blog/posts/under-construction-democratisation-in-bolivia',
'http://www.bolivianexpress.org/blog/posts/out-of-the-closet-into-the-fire',
'http://www.bolivianexpress.org/blog/posts/rainbow-nation',
'http://www.bolivianexpress.org/blog/posts/unlove-when-love-has-lost-its-llajwa',
'http://www.bolivianexpress.org/blog/posts/blind-love',
'http://www.bolivianexpress.org/blog/posts/live-music-reviews',
'http://www.bolivianexpress.org/blog/posts/musical-roundup',
'http://www.bolivianexpress.org/blog/posts/los-b',
'http://www.bolivianexpress.org/blog/posts/matame-por-favor',
'http://www.bolivianexpress.org/blog/posts/hamlet-de-los-andes',
'http://www.bolivianexpress.org/blog/posts/30-grados-de-frio',
'http://www.bolivianexpress.org/blog/posts/perfidia',
'http://www.bolivianexpress.org/blog/posts/monthly-review-la-casona',
'http://www.bolivianexpress.org/blog/posts/the-white-gold-lithium',
'http://www.bolivianexpress.org/blog/posts/the-end-of-the-world-as-we-know-it',
'http://www.bolivianexpress.org/blog/posts/a-united-front',
'http://www.bolivianexpress.org/blog/posts/ploughing-in-the-sea-the-legacy-of-bolivar-6-de-agosto',
'http://www.bolivianexpress.org/blog/posts/customary-moralety',
'http://www.bolivianexpress.org/blog/posts/constellation-sacaba',
'http://www.bolivianexpress.org/blog/posts/grand-designs-apocalyptic-architecture',
'http://www.bolivianexpress.org/blog/posts/marcos-and-bellas',
'http://www.bolivianexpress.org/blog/posts/music-money-can-t-buy',
'http://www.bolivianexpress.org/blog/posts/drumming-for-hate-s-a',
'http://www.bolivianexpress.org/blog/posts/the-maestro-departs',
'http://www.bolivianexpress.org/blog/posts/songs-of-freedom',
'http://www.bolivianexpress.org/blog/posts/charmed',
'http://www.bolivianexpress.org/blog/posts/tainted-love-private-investigators-in-la-paz',
'http://www.bolivianexpress.org/blog/posts/faces-of-el-alto-market',
'http://www.bolivianexpress.org/blog/posts/ho-ho-ho-and-a-pirate-dvd',
'http://www.bolivianexpress.org/blog/posts/senoras-y-senores',
'http://www.bolivianexpress.org/blog/posts/bolivia-my-new-furusato',
'http://www.bolivianexpress.org/blog/posts/matamba',
'http://www.bolivianexpress.org/blog/posts/jaime-saenz',
'http://www.bolivianexpress.org/blog/posts/vero-perez',
'http://www.bolivianexpress.org/blog/posts/getting-to-the-heart-of-it',
'http://www.bolivianexpress.org/blog/posts/expensive-smiles',
'http://www.bolivianexpress.org/blog/posts/kandinsky',
'http://www.bolivianexpress.org/blog/posts/ohh-la-la-ooh-la-paz',
'http://www.bolivianexpress.org/blog/posts/claudia-balderrama-bolivia-s-race-walker',
'http://www.bolivianexpress.org/blog/posts/bound-by-beauty',
'http://www.bolivianexpress.org/blog/posts/the-forgotten-towers',
'http://www.bolivianexpress.org/blog/posts/vidas-y-muertes',
'http://www.bolivianexpress.org/blog/posts/migrate-and-conquer',
'http://www.bolivianexpress.org/blog/posts/the-butcher-of-bolivia',
'http://www.bolivianexpress.org/blog/posts/political-femicide',
'http://www.bolivianexpress.org/blog/posts/bolivia-s-women-warriors',
'http://www.bolivianexpress.org/blog/posts/mujeres-creando',
'http://www.bolivianexpress.org/blog/posts/brickfast',
'http://www.bolivianexpress.org/blog/posts/things-you-didn-t-know-about-coca',
'http://www.bolivianexpress.org/blog/posts/open-your-head',
'http://www.bolivianexpress.org/blog/posts/the-incan-milky-way',
'http://www.bolivianexpress.org/blog/posts/nighttime-on-high',
'http://www.bolivianexpress.org/blog/posts/creatures-of-the-chacana',
'http://www.bolivianexpress.org/blog/posts/inti-wara-yassi',
'http://www.bolivianexpress.org/blog/posts/la-senda-verde',
'http://www.bolivianexpress.org/blog/posts/bolivian-wildlife-under-threat',
'http://www.bolivianexpress.org/blog/posts/animals-at-altitude',
'http://www.bolivianexpress.org/blog/posts/tall-tales-of-la-paz',
'http://www.bolivianexpress.org/blog/posts/run-gringo-run',
'http://www.bolivianexpress.org/blog/posts/salar-de-uyuni',
'http://www.bolivianexpress.org/blog/posts/rurrenabaque',
'http://www.bolivianexpress.org/blog/posts/death-road',
'http://www.bolivianexpress.org/blog/posts/drinking-in-la-paz',
'http://www.bolivianexpress.org/blog/posts/white-nights',
'http://www.bolivianexpress.org/blog/posts/lessons-from-the-booth',
'http://www.bolivianexpress.org/blog/posts/too-few-to-tango',
'http://www.bolivianexpress.org/blog/posts/living-the-death-road-part-3',
'http://www.bolivianexpress.org/blog/posts/fitaz',
'http://www.bolivianexpress.org/blog/posts/voices-from-the-fairground',
'http://www.bolivianexpress.org/blog/posts/honey-i-shrunk-a-festival',
'http://www.bolivianexpress.org/blog/posts/crossfest-santa-cruz',
'http://www.bolivianexpress.org/blog/posts/the-new-bolivian-fighters-cholitas-luchadoras',
'http://www.bolivianexpress.org/blog/posts/giving-the-game-away',
'http://www.bolivianexpress.org/blog/posts/get-your-moto-running',
'http://www.bolivianexpress.org/blog/posts/bolivia-under-the-knife',
'http://www.bolivianexpress.org/blog/posts/what-you-want-is-what-you-get',
'http://www.bolivianexpress.org/blog/posts/suspended-in-madness',
'http://www.bolivianexpress.org/blog/posts/every-day-miracles',
'http://www.bolivianexpress.org/blog/posts/land-of-healers',
'http://www.bolivianexpress.org/blog/posts/healing-in-small-doses',
'http://www.bolivianexpress.org/blog/posts/a-woman-s-mission-to-change-mining-in-bolivia',
'http://www.bolivianexpress.org/blog/posts/bolivia-s-clandestine-abortion-industry',
'http://www.bolivianexpress.org/blog/posts/protecting-the-sex-workers-profession-a-tragic-reality',
'http://www.bolivianexpress.org/blog/posts/women-sex-workers',
'http://www.bolivianexpress.org/blog/posts/women-and-cooking-a-cultural-connection',
'http://www.bolivianexpress.org/blog/posts/one-dollar-at-a-time-microfinance-in-bolivia',
'http://www.bolivianexpress.org/blog/posts/networking-bolivia',
'http://www.bolivianexpress.org/blog/posts/true-bolivianite-the-story-of-ametrine',
'http://www.bolivianexpress.org/blog/posts/if-it-cures-it-cures',
'http://www.bolivianexpress.org/blog/posts/amartelo-the-love-sickness',
'http://www.bolivianexpress.org/blog/posts/glossary',
'http://www.bolivianexpress.org/blog/posts/asi-es-pues-la-tierra-llama',
'http://www.bolivianexpress.org/blog/posts/taxi-trivia',
'http://www.bolivianexpress.org/blog/posts/bolivia-in-drag',
'http://www.bolivianexpress.org/blog/posts/in-this-fair-city',
'http://www.bolivianexpress.org/blog/posts/the-journey-of-the-dead',
'http://www.bolivianexpress.org/blog/posts/the-devil-s-in-the-detail',
'http://www.bolivianexpress.org/blog/posts/living-the-death-road-part-2',
'http://www.bolivianexpress.org/blog/posts/living-the-death-road',
'http://www.bolivianexpress.org/blog/posts/llama-foetuses',
'http://www.bolivianexpress.org/blog/posts/baking-for-the-dead',
'http://www.bolivianexpress.org/blog/posts/halloween-or-jailonween',
'http://www.bolivianexpress.org/blog/posts/the-living-skulls-of-the-dead',
'http://www.bolivianexpress.org/blog/posts/morir-en-la-paz',
'http://www.bolivianexpress.org/blog/posts/shalom-bolivia',
'http://www.bolivianexpress.org/blog/posts/nomadic-healing',
'http://www.bolivianexpress.org/blog/posts/ekeko',
'http://www.bolivianexpress.org/blog/posts/scattering-seeds-catholicism-and-the-pachamama',
'http://www.bolivianexpress.org/blog/posts/nazareth-flores-cabao-a-marcher-s-story',
'http://www.bolivianexpress.org/blog/posts/wiphala-relic-or-re-invention',
'http://www.bolivianexpress.org/blog/posts/turning-the-pages-bolivian-history-in-books',
'http://www.bolivianexpress.org/blog/posts/gran-poder',
'http://www.bolivianexpress.org/blog/posts/ch-alla',
'http://www.bolivianexpress.org/blog/posts/aymara-new-year',
'http://www.bolivianexpress.org/blog/posts/preste-mayor',
'http://www.bolivianexpress.org/blog/posts/night-at-the-museums',
'http://www.bolivianexpress.org/blog/posts/ser-cholita',
'http://www.bolivianexpress.org/blog/posts/back-to-aymara',
'http://www.bolivianexpress.org/blog/posts/ten-aymara-names-and-meanings',
'http://www.bolivianexpress.org/blog/posts/top-10-cultural-shocks',
'http://www.bolivianexpress.org/blog/posts/top-10-reasons-to-watch-quien-mato-a-la-llamita-blanca',
'http://www.bolivianexpress.org/blog/posts/best-night-spots',
'http://www.bolivianexpress.org/blog/posts/coroico',
'http://www.bolivianexpress.org/blog/posts/carnival-first-hand',
'http://www.bolivianexpress.org/blog/posts/danse-avec-eux',
'http://www.bolivianexpress.org/blog/posts/creating-carnival',
'http://www.bolivianexpress.org/blog/posts/dancing-devils-and-crazy-cucumbers',
'http://www.bolivianexpress.org/blog/posts/the-people-live-el-carnaval',
'http://www.bolivianexpress.org/blog/posts/forget-christmas',
'http://www.bolivianexpress.org/blog/posts/flaviada',
'http://www.bolivianexpress.org/blog/posts/around-and-about-in-la-paz',
'http://www.bolivianexpress.org/blog/posts/a-user-s-guide-to-getting-around-in-la-paz',
'http://www.bolivianexpress.org/blog/posts/paceno-style',
'http://www.bolivianexpress.org/blog/posts/one-last-august-rite',
'http://www.bolivianexpress.org/blog/posts/bolivia-s-real-death-road',
'http://www.bolivianexpress.org/blog/posts/my-big-fat-bolivian-wedding',
'http://www.bolivianexpress.org/blog/posts/my-super-sweet-fifteen',
'http://www.bolivianexpress.org/blog/posts/borracho-estaba-e-hice-una-pelicula',
'http://www.bolivianexpress.org/blog/posts/oye-profes-leave-those-kids-alone',
'http://www.bolivianexpress.org/blog/posts/coca-vs-cola',
'http://www.bolivianexpress.org/blog/posts/el-mundial-in-bolivia',
'http://www.bolivianexpress.org/blog/posts/oversight-to-overhaul',
'http://www.bolivianexpress.org/blog/posts/weaving-dreams',
'http://www.bolivianexpress.org/blog/posts/city-lights',
'http://www.bolivianexpress.org/blog/posts/bolivian-immigrants-in-brazil',
'http://www.bolivianexpress.org/blog/posts/londres-habia-sido-bien',
'http://www.bolivianexpress.org/blog/posts/ir-y-venir',
'http://www.bolivianexpress.org/blog/posts/the-homes-of-the-homeless',
'http://www.bolivianexpress.org/blog/posts/music-money-and-the-messiah-rocking-out-for-christ',
'http://www.bolivianexpress.org/blog/posts/it-s-a-dog-s-life-in-la-paz',
'http://www.bolivianexpress.org/blog/posts/a-new-beginning-for-bolivia-s-disabled',
'http://www.bolivianexpress.org/blog/posts/earning-my-stripes',
'http://www.bolivianexpress.org/blog/posts/the-culture-of-protest',
'http://www.bolivianexpress.org/blog/posts/tipnis',
'http://www.bolivianexpress.org/blog/posts/project-durazno',
'http://www.bolivianexpress.org/blog/posts/cochabamba-express',
'http://www.bolivianexpress.org/blog/posts/blonde-but-bolivian',
'http://www.bolivianexpress.org/blog/posts/from-africa-to-the-andes',
'http://www.bolivianexpress.org/blog/posts/go-gringo-go',
'http://www.bolivianexpress.org/blog/posts/luces-camara-accion',
'http://www.bolivianexpress.org/blog/posts/moving-mountains',
'http://www.bolivianexpress.org/blog/posts/invisible-heroes',
'http://www.bolivianexpress.org/blog/posts/we-ll-have-a-gay-old-time',
'http://www.bolivianexpress.org/blog/posts/hanging-out-with-the-lustrabotas',
'http://www.bolivianexpress.org/blog/posts/tall-white-and-english-speaking',
'http://www.bolivianexpress.org/blog/posts/recuperar-recuperar-el-litoral-y-el-ancho-mar',
'http://www.bolivianexpress.org/blog/posts/eduardo-calla',
'http://www.bolivianexpress.org/blog/posts/what-s-past-is-prologue',
'http://www.bolivianexpress.org/blog/posts/the-phantom-of-the-theatre',
'http://www.bolivianexpress.org/blog/posts/maphra-on',
'http://www.bolivianexpress.org/blog/posts/pacena',
'http://www.bolivianexpress.org/blog/posts/top-ten-street-and-market-foods',
'http://www.bolivianexpress.org/blog/posts/blue-nightclub-review',
'http://www.bolivianexpress.org/blog/posts/forum-nightclub-review',
'http://www.bolivianexpress.org/blog/posts/cafe-arabica-review',
'http://www.bolivianexpress.org/blog/posts/cafe-beirut-review',
'http://www.bolivianexpress.org/blog/posts/wagamama-review',
'http://www.bolivianexpress.org/blog/posts/maphrao-on-review',
'http://www.bolivianexpress.org/blog/posts/art-entity',
'http://www.bolivianexpress.org/blog/posts/leaves-and-lines',
'http://www.bolivianexpress.org/blog/posts/soundcheck-la-paz',
'http://www.bolivianexpress.org/blog/posts/in-my-country',
'http://www.bolivianexpress.org/blog/posts/stefan-johansson',
'http://www.bolivianexpress.org/blog/posts/tony-suarex-a-life-less-ordinary',
'http://www.bolivianexpress.org/blog/posts/gabriel-barcelo-simple-mind',
'http://www.bolivianexpress.org/blog/posts/mamani-mamani',
'http://www.bolivianexpress.org/blog/posts/malabaristas-we-meet-the-street-artists-of-la-paz',
'http://www.bolivianexpress.org/blog/posts/a-wondrous-wander-through-la-paz-an-errant-gringo-s-artistic-pursuits',
'http://www.bolivianexpress.org/blog/posts/vinetas-con-altura',
'http://www.bolivianexpress.org/blog/posts/comic-encounters-la-paz-s-comic-artists',
'http://www.bolivianexpress.org/blog/posts/un-traguito-mas',
'http://www.bolivianexpress.org/blog/posts/micro-bus',
'http://www.bolivianexpress.org/blog/posts/fashion'
]
b=0
date=str
title=str
tag0=[]
authors=[]
f=int
while b !=212: 
    html = scraperwiki.scrape(str(a[b]))
    root = lxml.html.fromstring(html)
    count=len(str(html))
    for el in root.cssselect("section#body_content"):
        for el1 in el.cssselect("time[datetime]"):
            date=el1.text
        for el2 in el.cssselect("h1"):
            title=el2.text
    scraperwiki.sqlite.save(unique_keys=['orden'],data={'orden':b,'date':date,'count':count,'title':title,'id':str(a[b])})
    tag0=[]
    authors=[]
    b=b+1