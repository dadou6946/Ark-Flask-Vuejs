<template>

    <!-- MAP -->
    <div id="map-container" class="z-depth-3">

        <div id="ark-map" class="indigo lighten-5 right">

            <!-- Lieux -->
            <div class="card hoverable"
                v-for="site of sites"
                v-bind:class="[site.color, site.type]"
                v-bind:id="'site'+site.id"
                @click="lastClick(site)"
                :key="site.id">

                <span v-html="site.name+site.id"></span>

                <!-- Jetons indices -->
                <div v-if="site.clue!=0"
                    id="clue_token"
                    class=""
                    v-html="site.clue>1?'x'+site.clue:''">
                </div>

                <!-- Investigateurs -->
                <transition-group name="fade">
                    <div class="investigator"
                        v-for="(char,index) of site.character"
                        v-bind:class="'investigator_'+(index+1)"
                        v-bind:id="char.replace(' ','_')"
                        v-html="char"
                        v-bind:key="index">
                    </div>
                </transition-group>

                <!-- Monstres -->
                <transition-group name="fade">
                    <div  class="monster truncate"
                        v-for="(mons,index) of site.monster"
                        v-bind:class="'monster_'+(index+1)"
                        v-bind:id="mons"
                        v-html="mons"
                        v-bind:key="index">
                    </div>
                </transition-group>

                <!-- Portails -->
                <transition name="fade">
                    <div class="portal_token valign-wrapper"
                        v-for="mark of site.portal"
                        :key="mark">
                        <span v-html="mark"></span>
                    </div>
                </transition>

                <!-- Marqueurs -->
                <transition-group name="fade">
                    <div class="token center-align"
                        v-for="port of site.marker"
                        v-bind:class="port+'_token'"
                        v-bind:key="port">
                        <span v-html="port"></span>
                    </div>
                </transition-group>

                <!-- Evenements -->
                <transition-group name="fade">
                    <div class="token center-align"
                        v-for="ev of site.event"
                        v-bind:class="'event_token'"
                        v-bind:key="ev">
                        <span v-html="ev"></span>
                    </div>
                </transition-group>

            </div>

            <!-- Lieux spéciaux -->
            <div class="special_site card hoverable"
                v-for="special of specials"
                v-bind:class="'special'+special.id"
                :key="special.id">

                <span v-html="special.name"></span>

                <!-- Investigateurs -->
                <transition-group name="fade">
                    <div class="investigator"
                        v-for="(char,index) of special.character"
                        v-bind:class="'investigator_'+(index+1)"
                        v-bind:id="char.name.replace(' ','_')"
                        v-html="char.name"
                        v-bind:key="index">
                    </div>
                </transition-group>

                <!-- Monstres -->
                <transition-group name="fade">
                    <div  class="monster truncate"
                        v-for="(mons,index) of special.monster"
                        v-bind:class="'monster_'+(index+1)"
                        v-bind:id="mons.name"
                        v-html="mons.name"
                        v-bind:key="index">
                    </div>
                </transition-group>

            </div>

            <!-- liaisons entre les rues -->
            <div v-for="road of roads"
                v-bind:id="'road'+road.id"
                v-bind:class="road.way">
            </div>

            <!-- fleches de monstre -->
            <span
                v-for="arrow of arrows"
                v-bind:id="'arrow'+arrow.id"
                v-bind:class="arrow.color+'-arrow'"
                v-html="arrow.color=='double'?'&#10146;':'&#10148;'">
            </span>
        </div>

        <!-- L'au delà -->
        <div id="beyond-map" class="indigo lighten-4 right">

            <!-- Lieux -->
            <div class="world card center-align hoverable"
                v-for="world of beyond">

                <div v-for="step of world.steps"
                    v-bind:class="step.position==1?'first':'second'">

                    <!-- Investigateurs -->
                    <transition-group name="fade">
                        <div class="beyond_investigator"
                            v-for="(char, index) of step.character"
                            v-bind:id="char.replace(' ','_')"
                            v-bind:class="step.position==1? 'inv_first':'inv_second'"
                            v-html="char"
                            v-bind:key="index">
                        </div>
                    </transition-group>
                </div>

                <span class="other_world" v-html="world.name" ></span>
            </div>
        </div>
    </div>

</template>

<script>

export default {
  props: [
    'investigators',
    'sites',
    'beyond',
    'specials',
    'monsters',
    'objects',
    'moves',
  ],
  data() {
    return {

      playerNumber: 2, // nombre de joueurs
      investigatorPreview: '',
      roads: [
        { id: '1', way: 'bar-h' },
        { id: '2', way: 'bar-h' },
        { id: '3', way: 'bar-h' },
        { id: '4', way: 'bar-h' },
        { id: '5', way: 'bar-h' },
        { id: '6', way: 'bar-v' },
        { id: '7', way: 'bar-v' },
        { id: '8', way: 'bar-v' },
        { id: '9', way: 'bar-v' },
        { id: '10', way: 'bar-v' },
        { id: '11', way: 'bar-v' },
        { id: '12', way: 'bar-v' },
        { id: '13', way: 'bar-c' },
        { id: '14', way: 'bar-c' },
        { id: '15', way: 'bar-c' },
        { id: '16', way: 'bar-c' },
        { id: '17', way: 'bar-c' },
        { id: '18', way: 'bar-c' },
        { id: '19', way: 'bar-c' },
        { id: '20', way: 'bar-c' },
        { id: '21', way: 'bar-c' },
        { id: '22', way: 'bar-c' },
        { id: '23', way: 'bar-c' },
        { id: '24', way: 'bar-c' },
        { id: '25', way: 'bar-c' },
        { id: '26', way: 'bar-c' },
        { id: '27', way: 'bar-c' },
        { id: '28', way: 'bar-c' },
        { id: '29', way: 'bar-c' },
        { id: '30', way: 'bar-c' },
        { id: '31', way: 'bar-c' },
        { id: '32', way: 'bar-c' },
        { id: '33', way: 'bar-c' },

        { id: '34', way: 'bar-c' },
        { id: '35', way: 'bar-c' },
        { id: '36', way: 'bar-c' },
        { id: '37', way: 'bar-c' },
        { id: '38', way: 'bar-c' },
      ],
      arrows: [
        { id: '1', color: 'white' },
        { id: '2', color: 'white' },
        { id: '3', color: 'white' },
        { id: '4', color: 'white' },
        { id: '5', color: 'white' },
        { id: '6', color: 'white' },
        { id: '7', color: 'white' },
        { id: '8', color: 'white' },
        { id: '9', color: 'white' },
        { id: '10', color: 'black' },
        { id: '11', color: 'black' },
        { id: '12', color: 'black' },
        { id: '13', color: 'black' },
        { id: '14', color: 'black' },
        { id: '15', color: 'black' },
        { id: '16', color: 'black' },
        { id: '17', color: 'black' },
        { id: '18', color: 'black' },
        { id: '19', color: 'double' },
        { id: '20', color: 'double' },
        { id: '21', color: 'double' },
        { id: '22', color: 'double' },
        { id: '23', color: 'double' },
        { id: '24', color: 'double' },
        { id: '25', color: 'double' },
        { id: '26', color: 'double' },
        { id: '27', color: 'double' },
        { id: '28', color: 'double' },
        { id: '29', color: 'double' },
        { id: '30', color: 'double' },
        { id: '31', color: 'double' },
        { id: '32', color: 'double' },
        { id: '33', color: 'double' },
        { id: '34', color: 'double' },
        { id: '35', color: 'double' },
        { id: '36', color: 'double' },
        { id: '37', color: 'double' },
        { id: '38', color: 'double' },
        { id: '39', color: 'double' },
        { id: '40', color: 'double' },
        { id: '41', color: 'double' },
        { id: '42', color: 'double' },
        { id: '43', color: 'double' },
        { id: '44', color: 'double' },
      ],

    };
  },
  methods: {
    lastClick(site) {
      // this.log(site)
      this.$emit('wasClicked', site);
    },
    log(message) {
      console.log(message);
    },
    continueAction() {
      // console.log('ici')
      this.$router.push('choose-ancient');
    },
    // Mise a jour de l'affichage des monstres et investigateurs
    updateMap() {
      // remise à zero et affichage
      this.rebootMap();
      this.updateSites();
    },
    // Vide de chaque lieux
    rebootMap() {
      this.sites.forEach((site) => {
        site.monster = [];
        site.character = [];
      });
    },
    // Remise a zero des joueurs perdus dans le temps et l'espace
    rebootLost() {
      this.specials[0].character = [];
    },
    // Affichage des investigateurs et monstres
    updateSites() {
      // Ajout des monstres sur la map
      this.monsters.forEach((monster) => {
        // Pour chacun des monstres dans monsters, on ajoute ce montre au site correspondant
        this.sites.find((site) => {
          if (site.id == monster.siteId) site.monster.push(monster.name);
        });
      });
      // Ajout des investigateurs sur la map
      this.investigators.forEach((investigator) => {
        // Pour chacun des investigateurs, on l'ajoute au site correspondant
        this.sites.find((site) => {
          if (site.id == investigator.siteId) site.character.push(investigator.name);
        });
      });
    },
    // retourne une classe différente de mise en valeur de site en fonction de son rang d'éloignement
    highlight(id) {
      console.log(id);
    },
  },
  mounted() {
    this.updateSites();
  },
};

</script>

<style>

        /***** MAP*****/
        #map-container
        {
            height : 710px;
            width: 1090px;
        }
        #button-container
        {
            height : 40px;
            width: 100%;
            margin-bottom: 25px;
        }
        #map-container, #button-container
        {
            margin-left: auto;
            margin-right: auto;
        }
        #ark-map
        {
            position : relative;
            height : 710px;
            width: 975px;
            /*background-color: lightgrey;*/
            padding-top: -50px;
        }

        #beyond-map
        {
            position : relative;
            height : 710px;
            width: 115px;
            /*background-color: lightgrey;*/
            padding: 5px;
            padding-top: 30px

        }

        /***** LIEUX *****/
        div .site, div .street, div .world, div .special_site
        {
            position : absolute;
            height: 80px;
            text-align: center;
            color: white;
            display:flex;
            justify-content:center;
            align-items:center;
            z-index: 10;
            text-shadow: 1px 1px 2px black;
        }
        div .site
        {
            width : 80px;
            border-radius: 20%;
        }
        div .street, div .special_site
        {
            width: 80px;
        }
        div .card
        {
            margin: 0;
        }
        div.world
        {
            height:75px;
            width: 105px;
            background-color: white;
            position: relative;
            border-radius: 5px;
            z-index: 0;
            margin-top: 4px;
            margin-bottom: 4px;

        }
        div.first, div.second
        {
            width: 50%;
            height: 100%;
        }
        div.first
        {
            background-color: grey;
            width: 50%;
            border-radius: 5px 0 0 5px;
        }
        span.other_world {
            position: absolute;
            z-index: 500;
            /*left: 0%;
            right: 0%;*/
        }
        div .special36
        {
            bottom: 2px;
            right: 2px;
        }
        div .special37
        {
            bottom: 2px;
            left: 2px;
        }
        div .special38
        {
            bottom: 90px;
            left: 2px;
        }
        div .special39
        {
            bottom: 90px;
            right: 2px;
        }


        /***** LIEU individuel *****/
        div #site1
        {
            top: 5px;
            left: 55px;
        }
        div #site2
        {
            top: 5px;
            left: 155px;
        }
        div #site3
        {
            top: 5px;
            left: 255px;
        }
        div #site4
        {
            top: 5px;
            left: 355px;
        }
        div #site5
        {
            top: 5px;
            left: 455px;
        }
        div #site6
        {
            top: 5px;
            left: 555px;
        }

        div #site7
        {
            top: 5px;
            right: 235px;
        }
        div #site8
        {
            top: 5px;
            right: 135px;
        }
        div #site9
        {
            top: 5px;
            right: 35px;
        }

        div #site10
        {
            top: 145px;
            left: 50px;
        }
        div #site11
        {
            top: 245px;
            left: 50px;
        }
        div #site12
        {
            top: 345px;
            left: 50px;
        }

        div #site13
        {
            top: 135px;
            right: 10px;
        }
        div #site14
        {
            top: 235px;
            right: 10px;
        }
        div #site15
        {
            top: 335px;
            right: 10px;
        }

        div #site16
        {
            top: 365px;
            left: 180px;
        }
        div #site17
        {
            top: 465px;
            left: 180px;
        }
        div #site18
        {
            top: 465px;
            left: 385px;
        }

        div #site19
        {
            top: 395px;
            right: 140px;
        }
        div #site20
        {
            top: 495px;
            right: 140px;
        }

        div #site21
        {
            bottom: 5px;
            left: 185px;
        }
        div #site22
        {
            bottom: 5px;
            left: 285px;
        }
        div #site23
        {
            bottom: 5px;
            left: 385px;
        }

        div #site24
        {
            bottom: 5px;
            right: 405px;
        }
        div #site25
        {
            bottom: 5px;
            right: 305px;
        }
        div #site26
        {
            bottom: 5px;
            right: 205px;
        }


        div #site27
        {
            top: 105px;
            left: 155px;
        }
        div #site28
        {
            top: 105px;
            left: 455px;
        }
        div #site29
        {
            top: 105px;
            right: 135px;
        }
        div #site30
        {
            top: 245px;
            left: 155px;
        }
        div #site31
        {
            top: 235px;
            right: 115px;
        }
        div #site32
        {
            top: 365px;
            left: 285px;
        }
        div #site33
        {
            top: 395px;
            right: 245px;
        }
        div #site34
        {
            bottom: 105px;
            left: 285px;
        }
        div #site35
        {
            bottom: 105px;
            right: 305px;
        }

        /***** COULEURS *****/
        div .orange
        {
            background-color : orange;
        }
        div .white
        {
            background-color : #B5B4B3; color: black;
            text-shadow: 0px 0px 0px white;
        }
        div .grey
        {
            background-color: #656364;
        }
        div .green
        {
            background-color: #0b700b;
        }
        div .purple
        {
            background-color: #633E87;
        }
        div .yellow
        {
            background-color: #F9E46B;
        }
        div .blue
        {
            background-color: #41a3ef;
        }
        div .red
        {
            background-color: #CB191F;
        }
        div .brown
        {
            background-color: #631E15;
        }
        /***** liens entre les lieux *****/
        div .bar-h, div .bar-v, div .bar-c
        {
            background-color : white;
            box-shadow: 1px 2px 2px lightgrey;
            position: absolute;
            z-index: 0;
        }
        div .bar-h
        {
            height: 4px;
        }
        div .bar-v, div .bar-c
        {
            width: 4px;
        }

        div #road1
        {
            width: 270px;
            top: 135px;
            left : 205px;
        }
        div #road2
        {
            width: 270px;
            top: 135px;
            right : 205px;
        }
        div #road3
        {
            width: 370px;
            top: 415px;
            right : 255px;
        }
        div #road4
        {
            width: 280px;
            bottom: 145px;
            right : 355px;
        }
        div #road5
        {
            width: 560px;
            top: 280px;
            right : 185px;
        }
        div #road6
        {
            height: 80px;
            top: 175px;
            left : 195px;
        }
        div #road7
        {
            height: 120px;
            bottom: 170px;
            left : 325px;
        }
        div #road8
        {
            height: 180px;
            bottom: 290px;
            left : 275px;
            transform: rotate(-55deg);
        }
        div #road9
        {
            height: 200px;
            bottom: 260px;
            right : 215px;
            transform: rotate(55deg);
        }
        div #road10
        {
            height: 120px;
            bottom: 155px;
            right : 305px;
            transform: rotate(45deg);
        }
        div #road11
        {
            height: 350px;
            top: 50px;
            left : 315px;
            transform: rotate(65deg);
        }
        div #road12
        {
            height: 80px;
            top: 175px;
            right : 160px;
            transform: rotate(-25deg);
        }

        div #road13
        {
            height: 50px;
            top: 75px;
            right : 175px;
        }
        div #road14
        {
            height: 50px;
            top: 75px;
            right : 475px;
        }
        div #road15
        {
            height: 50px;
            top: 75px;
            left : 195px;
        }
        div #road16
        {
            height: 50px;
            bottom: 75px;
            left : 325px;
        }
        div #road17
        {
            height: 50px;
            bottom: 75px;
            right : 345px;
        }
        div #road18
        {
            height: 50px;
            bottom: 245px;
            right : 225px;
            transform:rotate(90deg);
        }
        div #road19
        {
            height: 50px;
            bottom: 275px;
            left : 275px;
            transform:rotate(90deg);
        }
        div #road20
        {
            height: 50px;
            bottom: 395px;
            left : 145px;
            transform:rotate(90deg);
        }
        div #road21
        {
            height: 50px;
            bottom: 405px;
            right : 95px;
            transform:rotate(90deg);
        }
        div #road22
        {
            height: 80px;
            top: 45px;
            left : 255px;
            transform:rotate(45deg);
        }
        div #road23
        {
            height: 80px;
            top: 40px;
            left : 125px;
            transform:rotate(-45deg);
        }
        div #road24
        {
            height: 80px;
            top: 40px;
            left : 425px;
            transform:rotate(-45deg);
        }
        div #road25
        {
            height: 80px;
            top: 40px;
            right : 240px;
            transform:rotate(-45deg);
        }
        div #road26
        {
            height: 80px;
            top: 40px;
            right : 110px;
            transform:rotate(45deg);
        }
        div #road27
        {
            height: 80px;
            top: 40px;
            right : 410px;
            transform:rotate(45deg);
        }
        div #road28
        {
            height: 80px;
            top: 175px;
            right : 90px;
            transform:rotate(45deg);
        }
        div #road29
        {
            height: 80px;
            top: 295px;
            right : 90px;
            transform:rotate(-45deg);
        }
        div #road30
        {
            height: 80px;
            top: 180px;
            left : 130px;
            transform:rotate(-45deg);
        }
        div #road31
        {
            height: 80px;
            top: 300px;
            left : 140px;
            transform:rotate(45deg);
        }
        div #road32
        {
            height: 80px;
            top: 420px;
            left : 270px;
            transform:rotate(45deg);
        }
        div #road33
        {
            height: 80px;
            top: 420px;
            left : 375px;
            transform:rotate(-45deg);
        }
        div #road34
        {
            height: 80px;
            bottom: 50px;
            left : 270px;
            transform:rotate(45deg);
        }
        div #road35
        {
            height: 80px;
            bottom: 50px;
            left : 375px;
            transform:rotate(-45deg);
        }
        div #road36
        {
            height: 80px;
            bottom: 50px;
            right : 400px;
            transform:rotate(45deg);
        }
        div #road37
        {
            height: 80px;
            bottom: 50px;
            right : 290px;
            transform:rotate(-45deg);
        }
        div #road38
        {
            height: 80px;
            bottom: 180px;
            right : 225px;
            transform:rotate(-45deg);
        }

        /****** FLECHES ******/
        .white-arrow, .black-arrow, .double-arrow
        {
            position: absolute;
            z-index: 0;
        }
        .white-arrow
        {
            font-size: 25px;
            color:white;
            text-shadow: 1px 1px 2px black;
        }
        .black-arrow
        {
            font-size: 25px;
            color:black;
        }
        .double-arrow
        {
            color:black;
            font-size: 35px;
        }
        #arrow1
        {
            left: 228px;
            top: 116px;
        }
        #arrow2
        {
            left: 529px;
            top: 116px;
        }
        #arrow3
        {
            right: 156px;
            top: 172px;
            transform:rotate(70deg);
        }
        #arrow4
        {
            right: 160px;
            top: 302px;
            transform:rotate(150deg);
        }
        #arrow5
        {
            right: 278px;
            top: 465px;
            transform:rotate(140deg);
        }
        #arrow6
        {
            right: 380px;
            bottom: 125px;
            transform:rotate(180deg);
        }
        #arrow7
        {
            left: 312px;
            bottom: 173px;
            transform:rotate(-90deg);
        }
        #arrow8
        {
            left: 306px;
            bottom: 330px;
            transform:rotate(-150deg);
        }
        #arrow9
        {
            left: 182px;
            top: 220px;
            transform:rotate(-90deg);
        }
        #arrow10
        {
            left: 436px;
            top: 120px;
            transform:rotate(-180deg);
        }
        #arrow11
        {
            right: 209px;
            top: 120px;
            transform:rotate(-180deg);
        }
        #arrow12
        {
            right: 144px;
            top: 212px;
            transform:rotate(250deg);
        }
        #arrow13
        {
            right: 262px;
            top: 371px;
            transform:rotate(320deg);
        }
        #arrow14
        {
            right: 322px;
            top: 501px;
            transform:rotate(320deg);
        }
        #arrow15
        {
            left: 359px;
            bottom: 129px;
        }
        #arrow16
        {
            left: 317px;
            bottom: 240px;
            transform:rotate(90deg);
        }
        #arrow17
        {
            left: 229px;
            bottom: 392px;
            transform:rotate(45deg);
        }
        #arrow18
        {
            left: 187px;
            top: 173px;
            transform:rotate(90deg);
        }

        #arrow19
        {
            left: 118px;
            top: 58px;
            transform:rotate(45deg);
        }
        #arrow20
        {
            left: 182px;
            top: 60px;
            transform:rotate(90deg);
        }
        #arrow21
        {
            left: 242px;
            top: 60px;
            transform:rotate(135deg);
        }

        #arrow22
        {
            left: 417px;
            top: 58px;
            transform:rotate(45deg);
        }
        #arrow23
        {
            left: 483px;
            top: 60px;
            transform:rotate(90deg);
        }
        #arrow24
        {
            left: 542px;
            top: 60px;
            transform:rotate(135deg);
        }
        #arrow25
        {
            right: 218px;
            top: 58px;
            transform:rotate(45deg);
        }
        #arrow26
        {
            right: 158px;
            top: 60px;
            transform:rotate(90deg);
        }
        #arrow27
        {
            right: 96px;
            top: 60px;
            transform:rotate(135deg);
        }
        #arrow28
        {
            right: 73px;
            top: 190px;
            transform:rotate(135deg);
        }
        #arrow29
        {
            right: 73px;
            top: 256px;
            transform:rotate(180deg);
        }
        #arrow30
        {
            right: 75px;
            top: 312px;
            transform:rotate(225deg);
        }
        #arrow31
        {
            left: 116px;
            top: 192px;
            transform:rotate(45deg);
        }
        #arrow32
        {
            left: 113px;
            top: 262px;
        }
        #arrow33
        {
            left: 113px;
            top: 323px;
            transform:rotate(-45deg);
        }
        #arrow34
        {
            left: 243px;
            top: 382px;
        }
        #arrow35
        {
            left: 243px;
            top: 443px;
            transform:rotate(-45deg);
        }
        #arrow36
        {
            left: 367px;
            top: 443px;
            transform:rotate(-135deg);
        }
        #arrow37
        {
            left: 247px;
            bottom: 59px;
            transform:rotate(-45deg);
        }
        #arrow38
        {
            left: 308px;
            bottom: 57px;
            transform:rotate(-90deg);
        }
        #arrow39
        {
            left: 367px;
            bottom: 55px;
            transform:rotate(-135deg);
        }
        #arrow40
        {
            right: 392px;
            bottom: 60px;
            transform:rotate(-45deg);
        }
        #arrow41
        {
            right: 332px;
            bottom: 57px;
            transform:rotate(-90deg);
        }
        #arrow42
        {
            right: 268px;
            bottom: 55px;
            transform:rotate(-135deg);
        }
        #arrow43
        {
            right: 205px;
            bottom: 185px;
            transform:rotate(-135deg);
        }
        #arrow44
        {
            right: 203px;
            top: 416px;
            transform:rotate(180deg);
        }

        /***** JETONS *****/
        #clue_token
        {
            color: white;
            top: -3px;
            right: -4px;
            height: 30px;
            width: 30px;
            background-color: lightgreen;
            background-image: url("/image/token/clue.png");
            background-size: contain;
            background-repeat: no-repeat;
            padding-top: 1rem;
            font-size: 12px;
            /*filter: opacity(70%);*/
            /*-webkit-filter: opacity(70%);*/
        }
        .token
        {
            height: 35px;
            width: 35px;
            background-color: lightgrey;
        }
        .token, #clue_token, .portal_token,
        div#Jenny_Barnes, div#Peggy_Green, div#Francis_Sailor, div#Joe_Diamond, div#Daisie_Walker, div#Anne_Hathaway, div#Mark_Harrigan
        {
            position: absolute;
            z-index: 999;
            background-size: contain;
            background-repeat: no-repeat;
            border-radius: 50%;
            -webkit-box-shadow: 2px 2px 0px 0px rgba(0,0,0,0.65);
            -moz-box-shadow: 2px 2px 0px 0px rgba(0,0,0,0.65);
            box-shadow: 2px 2px 0px 0px rgba(0,0,0,0.65);
        }
        div.monster
        {
            position: absolute;
            z-index: 999;
            /*background-size: contain;*/
            /*background-repeat: no-repeat;*/
            border-radius: 5px;
            -webkit-box-shadow: -1px 1px 2px 0px rgba(0,0,0,0.65);
            -moz-box-shadow: -1px 1px 2px 0px rgba(0,0,0,0.65);
            box-shadow: -1px 1px 2px 0px rgba(0,0,0,0.65);
            /*font-size: 12px;*/
            background-color: lightgrey;
            height: 30px;
            width: 42px;
        }
        div.monster_1
        {
            top:-2px;
            left:-2px;
        }
        div.monster_2
        {
            top:-2px;
            left:18px;
        }
        div.monster_3
        {
            top:-2px;
            left:38px;
        }
        div.monster_4
        {
            top:-2px;
            left:58px;
        }

        div.investigator, div.beyond_investigator
        {
            background-color: grey;
            height: 35px;
            width: 35px;
        }

        div.investigator_1
        {
            bottom: 0;
            right: 5px;
        }
        div.investigator_2
        {
            bottom: 0;
            right: 20px;
        }
        div.investigator_3
        {
            bottom: 0;
            right: 35px;
        }
        div.investigator_4
        {
            bottom: 0;
            right: 50px;
        }
        div.investigator_5
        {
            bottom: 30px;
            right: 5px;
        }
        div.investigator_6
        {
            bottom: 30px;
            right: 20px;
        }
        .portal_token
        {
            top: 15px;
            height: 45px;
            width: 45px;
            background-color: black;
            color: white;
            /*background-image: url(img/portal/hallCelano.png);*/
        }
        div.event_token
        {
            background-color: red;
        }

        /*TRANSITIONS*/
        .fade-enter-active, .fade-leave-active {
            transition: opacity .75s;
        }
        .fade-enter, .fade-leave-to
        {
            opacity: 0;
        }

                /*BOUTTONS GROUPES*/
        .btn-group {
          position: relative;
          display: -ms-inline-flexbox;
          display: inline-flex;
          vertical-align: middle;
        }

        .btn-group>.btn:first-child:not(:last-child) {
          border-top-right-radius: 0;
          border-bottom-right-radius: 0;
        }

        .btn-group>.btn:not(:first-child):not(:last-child) {
          border-radius: 0;
        }

        .btn-group>.btn:last-child:not(:first-child),
        .btn-group>.dropdown-toggle:not(:first-child) {
          border-top-left-radius: 0;
          border-bottom-left-radius: 0;
        }

        .btn-group>.btn-inactive {
          background-color: #607d8b;
        }

        .btn-group>.btn {
          -webkit-box-shadow: 0 0px 0px 0 rgba(0, 0, 0, 0), 0 0px 0px 0px rgba(0, 0, 0, 0), 0 0px 0px 0 rgba(0, 0, 0, 0);
          box-shadow: 0 0px 0px 0 rgba(0, 0, 0, 0), 0 0px 0px 0px rgba(0, 0, 0, 0), 0 0px 0px 0 rgba(0, 0, 0, 0);
        }

        .btn-group>.btn-inactive:hover {
          background-color: #728F9D;
        }

        .btn-group>.btn:hover {
          -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.12), 0 1px 5px 0 rgba(0, 0, 0, 0.2);
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.12), 0 1px 5px 0 rgba(0, 0, 0, 0.2);
        }

</style>
