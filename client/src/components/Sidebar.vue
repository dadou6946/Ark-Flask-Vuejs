<template>
    <div>
        <!-- SIDEBARS APPARAISANT AU CLIQUE SUR LES BOUTONS -->

        <!-- PANNEAU INVESTIGATEURS -->
        <transition name="fade">
            <nav id="sidebar-investigator"
                v-if="navbar.investigator"
                class="grey sidenav sidenav-fixed">

                <!-- BOUTONS D'INVESTIGATEURS -->
                <div class="center-align">
                    <button class="waves-effect waves-grey grey darken-2 btn btn-small character-button"
                        v-for="(investigator, index) of investigators"
                        @click="showInvestigator(investigator.name)"
                        :key="index">
                        <span v-html="investigator.name"></span>
                    </button>
                </div>

                <div class="divider"></div>

                <!-- Fiche INVESTIGATEUR -->
                <transition name="fade" mode="out-in">
                    <div v-for="investigator of investigators"
                        v-if="investigatorPreview!='' && investigator.name == investigatorPreview"
                        :key="investigator.name">
                        <div class="row center-align lh-15">
                            <!-- IMAGE -->
                            <img class="grey lighten-3 z-depth-3 photo-character"
                                :src="'/image/sheet/character/head/'+investigatorPreview.replace(' ', '')+'.png'"
                                :alt="investigatorPreview">
                            <!-- INFORMATIONS  -->
                            <div class="col m6">
                                <h5 id="name">{{investigator.name}}</h5>
                                <span id="profession">La Diletante</span>
                                <div class="divider"></div>
                                <span id="sanity">Santé mentale: 6/6</span><br>
                                <span id="stamina">Résistance: 4/4</span><br>
                                <div class="divider"></div>
                                <span id="statut">Statut: ok</span>
                            </div>
                        </div>

                        <div class="divider"></div>

                        <div class="row">
                            <!-- POSSESSIONS, MAISON ET CONCENTRATION -->
                            <div class="col m6 lh-15 left-content">
                                <span id="house">Maison: </span><span>Gare</span>
                                <div class="divider"></div>
                                <span>Possessions fixes :</span><br>
                                <span>10$</span><br>
                                <span>Possessions aléatoires :</span><br>
                                <span>1 Compétence, 1 Sort, 1 Objet Unique, 2 Objets Communs</span>
                                <div class="divider"></div>
                                <span>Concentration: 1</span>
                            </div>
                            <!-- COMPÉTENCES SPÉCIALES -->
                            <div class="col m6 justified-text">
                                <span class="lh-15">Héritage</span><br><br>
                                <span id="capacity-text">
                                    <!-- <b>Entretien:</b> Jenny gagne 1$. -->
                                    <b>Entretien:</b> Les monstres et les portails ne peuvent pas apparaitre a l'endroit ou se trouve Kate à cause de son stabilitisateur de flux. Les monstres et les portails ne disparaissent cependant pas quand elle rentre dans un lieu, et les monstres peuvent entre normalement dans un lieu ou elle se trouve.
                                </span>
                            </div>
                        </div>

                        <div class="divider"></div>

                        <div class="row lh-15">
                            <!-- TEXTES D'APTITUDES -->
                            <div class="col m4">
                                <div class="skills mt-5">
                                    <div>vitesse :</div>
                                    <div>discretion:</div>
                                </div>
                                <div class="skills mt-25">
                                    <div>vigueur:</div>
                                    <div>volonté:</div>
                                </div>
                                <div class="skills mt-25">
                                    <div>savoir:</div>
                                    <div>chance:</div>
                                </div>
                            </div>
                            <!-- VALEURS ET GLOBULES -->
                            <div class="col m8">
                                <div v-for="(skills,index) of investigator.availableSkills" class="row row-skills center-align">
                                    <div v-for="(value) of skills"
                                        class="col m3 skill"
                                        v-html="value"
                                        v-bind:class="investigator.skills[index] == value?globule(index):''">
                                    </div>
                                    <br>
                                    <div v-if="index =='discretion' || index =='volonte'" v-html="'<br>'"></div>
                                </div>
                            </div>
                        </div>

                        <div class="divider"></div>

                        <!-- ARGENT, INDICES ET POSITION -->
                        <div class="row lh-15">
                            <div class="col m6">
                                <span>Argent : 10$</span>
                            </div>
                            <div class="col m6">
                                <span>Indices : <img id="clue-token-img" :src="'/image/token/clue.png'" alt="indices"> X 2</span><br>
                            </div>
                            <div class="col m12">
                                <span>Position : Journal</span>
                            </div>
                        </div>

                        <!-- BOUTONS D'OBJETS -->
                        <div class="row lh-15 center-align">
                            <div class="col m12">
                                <button class="waves-effect waves-green green darken-1 btn character-button">
                                    Compétences
                                    <img class="button-icon-small" :src="'/image/icon/parchment.png'" alt="competences">
                                </button>
                                <button class="waves-effect waves-green green darken-1 btn character-button">
                                    Objets
                                    <img class="button-icon-small" :src="'/image/icon/object.png'" alt="objets">
                                </button>
                                <button class="waves-effect waves-green green darken-1 btn character-button">
                                    Alliés
                                    <img class="button-icon-small" :src="'/image/icon/ally.png'" alt="allies">
                                </button>
                            </div>
                            <div class="col m12">
                                <button class="waves-effect waves-green green darken-1 btn character-button">
                                    Trophés
                                    <img class="button-icon-small" :src="'/image/icon/trophy.png'" alt="trophees">
                                </button>
                                <button class="waves-effect waves-green green darken-1 btn character-button">
                                    Objets spéciaux
                                    <img class="button-icon-small" :src="'/image/icon/special.png'" alt="objets speciaux">
                                </button>
                            </div>
                        </div>

                    </div>
                </transition>
            </nav>
        </transition>

        <!-- PANNEAU GARDIEN -->
        <transition name="fade">
            <nav id="sidebar-guardian" class="sidenav grey green darken-1"
                v-if="navbar.guardian">
            </nav>
        </transition>

        <!-- PANNEAU INFOS DE PARTIE -->
        <transition name="fade">
            <nav id="sidebar-game" class="grey darken-2"
                 v-if="navbar.game">
                <div class="container">
                    <div class="row lh-15 mt-25">
                        <div class="col m6">
                            <span>Tour n° 2</span><br>
                            <span>Phase : Mouvement</span><br>
                            <span>Premier joueur : joueur 1 - Francis Sailor</span><br>
                            <span>Joueur actuel : joueur 1 - Francis Sailor</span><br>
                            <span>Nombre de joueurs : 4</span><br>
                            <button class="waves-effect waves-teal btn btn-small character-button">Conditions de victoire</button>
                            <button class="waves-effect waves-teal btn btn-small character-button">Conditions de Défaite</button>
                            <!-- <ul>
                                <li>Sceller 6 portails</li>
                                <li>Battre le grand Ancien</li>
                                <li></li>
                                <li></li>
                            </ul> -->

                        </div>
                        <div class="col m6">
                            <span>Environnement actif : aucun</span><br>
                            <span>Rumeur active : aucune</span><br>
                            <span>Niveau de terreur : 1/12</span><br>
                            <span>Lieux fermés : aucun</span><br>
                            <span>Echelle de l'ancien : 1/12</span><br>
                            <span>Monstres en jeu/ nombre maximum : 2 / 6</span><br>
                            <span>Monstres dans la périphérie/ nombre maximum : 0 / 6</span><br>
                            <span>Portail actifs / nombre maximum : 1 / 6</span><br>
                        </div>
                    </div>
                </div>
            </nav>
        </transition>

        <!-- PANNEAU HERAUT -->
        <transition name="fade">
            <nav id="sidebar-herald" class="grey green darken-1"
                v-if="navbar.herald">
            </nav>
        </transition>

        <!-- PANNEAU ANCIENT -->
        <transition name="fade">
            <nav id="sidebar-ancient"
                class="grey lh-15"
                v-if="navbar.ancient">
                <div class="row center-align">
                    <!-- IMAGE DE L'ANCIEN -->
                    <img :src="'/image/sheet/ancient/head/'+ ancient.name +'.png'"
                        class="col m12 col moffset-1 grey lighten-3 z-depth-3"
                        style="padding:6px;"
                        :alt="ancient.name">
                    <!-- NOM -->
                    <div class="col m12">
                        <h5 id="name" class="center-align">{{ancient.name}}</h5>
                    </div>
                    <!-- VALEUR DE COMBAT -->
                    <div class="col m6">
                        <span id="combatValue">{{ancient.combatValue}}</span>
                    </div>
                    <!-- CAPACITE DEFENSIVE -->
                    <div class="col m6">
                        <span id="defensiveAbility">{{ancient.defensiveAbility.join(', ')}}</span>
                    </div>
                </div>
                <div class="divider"></div>
                <!-- TEXTES DE COMPÉTENCES D'ANCIEN -->
                <div class="row">
                    <div class="col m6">
                        <div class="justified-text">
                            <b>Adorateurs</b><br>
                            <span>{{ ancient.adorer.text }}</span>
                        </div>
                    </div>
                    <div class="col m6">
                        <div class="justified-text">
                            <b>{{ ancient.power.title }}</b><br>
                            <span>{{ ancient.power.text }}</span>
                            <div class="divider"></div>
                            <b v-if="ancient.battleEvent">Début de bataille</b>
                            <span v-if="ancient.battleEvent">{{ ancient.battleEvent.text }}</span>
                        </div>
                    </div>
                </div>
                <div class="divider"></div>
                <div class="row">
                    <div class="col m12">
                        <b>Attaque</b><br>
                        <span>{{ ancient.attack.text }}</span>
                    </div>
                </div>
                <div class="divider"></div>
                <!-- ECHELLE DE L'ANCIEN -->
                <div class="row">
                    <div class="col m12 mt-25">
                        <div class="col m2 center-align"
                            v-for="n in ancient.ladder.maximum">
                            <div class="green valign-wrapper z-depth-3 ancient-number-ladder">
                                {{ n }}
                                <!-- PIONS DESTIN -->
                                <img :src="'/image/token/destin.jpg'"
                                    v-if="n <= ancient.ladder.current"
                                    class="destiny-token"
                                    alt="marqueur_destin">
                            </div>
                        </div>
                    </div>
                </div>

            </nav>
        </transition>


        <!-- BOUTONS AFFICHANT LES SIDEBARS-->
        <div id="button-container" class="center-align green card">

            <!-- INVESTIGATEURS -->
            <button class="waves-effect waves-light btn grey"
                :class="(navbar.investigator ? 'darken-2' : '')"
                @click="switchNavbar('investigator')">
                <img class="button-icon" :src="'/image/icon/characters.png'" alt="joueurs">
                joueurs <b>{{ navbar.investigator==false?'+':'-' }}</b>
            </button>

            <!-- GARDIEN -->
            <button class="waves-effect waves-light btn grey"
                :class="(navbar.guardian ? 'darken-2' : '')"
                @click="switchNavbar('guardian')">
                <img class="button-icon" :src="'/image/icon/guardian.png'" alt="gardien">
                Gardien <b>{{ navbar.guardian==false?'+':'-' }}</b>
            </button>

            <!-- INFORMATIONS DE LA PARTIE -->
            <button class="waves-effect waves-light btn grey"
                :class="(navbar.game ? 'darken-2' : '')"
                @click="switchNavbar('game')">
                <img class="button-icon" :src="'/image/icon/info.png'" alt="informations">
                Infos <b>{{ navbar.game==false?'+':'-' }}</b>
            </button>

            <!-- HERAUT -->
            <button class="waves-effect waves-light btn grey"
                :class="(navbar.herald ? 'darken-2' : '')"
                @click="switchNavbar('herald')">
                <img class="button-icon" :src="'/image/icon/herald.png'" alt="heraut">
                Héraut <b>{{ navbar.herald==false?'+':'-' }}</b>
            </button>

            <!-- ANCIEN -->
            <button class="waves-effect waves-light btn grey"
                :class="(navbar.ancient ? 'darken-2' : '')"
                @click="switchNavbar('ancient')">
                <img class="button-icon" :src="'/image/icon/cthulhu.png'" alt="ancien">
                Ancien <b>{{ navbar.ancient==false?'+':'-'}}</b>
            </button>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {

      navbar:
                    {
                      investigator: false,
                      ancient: false,
                      game: false,
                      guardian: false,
                      herald: false,
                    },
      investigators: [
        {
          name: 'Joe Diamond',
          skills: {
            vitesse: 3, discretion: 4, vigueur: 2, volonte: 3, savoir: 0, chance: 3,
          },
          availableSkills: {
            vitesse: [3, 4, 5, 6], discretion: [4, 3, 2, 1], vigueur: [2, 3, 4, 5], volonte: [3, 2, 1, 0], savoir: [0, 1, 2, 3], chance: [3, 2, 1, 0],
          },
          objects: ['Automatique 45'],
        },
        {
          name: 'Francis Sailor',
          skills: {
            vitesse: 1, discretion: 5, vigueur: 1, volonte: 3, savoir: 1, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [5, 4, 3, 2], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [1, 2, 3, 4], chance: [5, 4, 3, 2],
          },
          objects: ['Manteau sombre', 'Motocyclette'],
        },
        {
          name: 'Jenny Barnes',
          skills: {
            vitesse: 0, discretion: 3, vigueur: 2, volonte: 3, savoir: 0, chance: 4,
          },
          availableSkills: {
            vitesse: [0, 1, 2, 3], discretion: [3, 2, 1, 0], vigueur: [2, 3, 4, 5], volonte: [3, 2, 1, 0], savoir: [0, 1, 2, 3], chance: [4, 3, 2, 0],
          },
          objects: ['Dynamite', 'Lance-flammes', 'Hache', 'Grigri'],
        },
        {
          name: 'Daisy Walker',
          skills: {
            vitesse: 1, discretion: 4, vigueur: 1, volonte: 3, savoir: 2, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [4, 3, 2, 1], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [2, 3, 4, 5], chance: [5, 4, 3, 2],
          },
          objects: ['Croix', 'Lanterne'],
        },
        {
          name: 'Peggy Green',
          skills: {
            vitesse: 1, discretion: 4, vigueur: 1, volonte: 3, savoir: 2, chance: 5,
          },
          availableSkills: {
            vitesse: [1, 2, 3, 4], discretion: [4, 3, 2, 1], vigueur: [1, 2, 3, 4], volonte: [3, 2, 1, 0], savoir: [2, 3, 4, 5], chance: [5, 4, 3, 2],
          },
          objects: ['Porte bonheur'],
        },
      ],
      investigatorPreview: '',
      ancient:
                {
                  name: 'Yig',
                  combatValue: '-3',
                  defensiveAbility: ['Aucun'],
                  adorer: {
                    text: 'Les adorateurs de Yig sont en réalité des membres du Peuple Serpent déguisés. Leur morsure est très venimeuse. Les Cultistes ont une valeur de combat de +0 et des dégâts de combat de 4 résistances.',
                  },
                  power: {
                    title: 'La colère de Yig',
                    text: "Tant que Yig est plongé dans son sommeil, il gagne un pion destin quand un cultiste est battu ou quand un investigateur est perdu dans le temps et l'espace.",
                  },
                  battleEvent: {
                    text: 'Chaque investigateur est Maudit. Un investigateur qui est déjà Maudit est dévoré.',
                  },
                  attack: {
                    text: 'Chaque investigateur doit réussir un test de Vitesse (+1) ou perdre 1 Santé Mentale et 1 Résistance. Le modificateur de test diminue de 1 à chaque tour (+0 au deuxième tour, -1 au troisième, etc.)',
                  },
                  ladder: {
                    current: 3,
                    maximum: 14,
                  },
                },

    };
  },
  methods: {

    log(message) {
      console.log(message);
    },
    switchNavbar(libelle) {
      this.navbar[libelle] = !this.navbar[libelle];
    },
    showInvestigator(name) {
      this.investigatorPreview = name;
    },
    continueAction() {
      // console.log('ici')
      // this.$router.push('choose-ancient')
    },
    globule(index) {
      switch (index) {
        case 'vitesse':
        case 'vigueur':
        case 'savoir':
          return 'glob-top';
        case 'discretion':
        case 'volonte':
        case 'chance':
          return 'glob-bot';
      }
    },
  },
};

</script>

<style>

    /* BOUTONS */
    button.character-button
    {
        margin:3px;
        border-radius:5px;
        font-size:10px;
        line-height: normal;
    }

    img.button-icon
    {
        height:25px;
        margin-right:7px;
        padding-top: 7px;
    }

    img.button-icon-small
    {
        height:15px;
        margin-left:7px;
    }

    /* SIDEBARS */
    #sidebar-investigator
    {
        transform: translateX(0px);
        z-index:980;
        width:370px;
        line-height:8pt;
    }

    #sidebar-guardian
    {
        transform: translateX(0px);
        z-index:990;
        height:100%;
        width:280px;
        position:absolute;
        right:0;
    }

    #sidebar-game
    {
        z-index:1000;
        width:100%;
        height:300px;
        position:absolute;
        bottom:0;
    }

    #sidebar-ancient
    {
        z-index:980;
        height:100%;
        width:370px;
        position:absolute;
        right:0;
    }

    #sidebar-herald
    {
        z-index:990;
        height:100%;
        width:280px;
        position:absolute;
        right:0;
    }

    /*TRANSITIONS*/
    .fade-enter-active, .fade-leave-active
    {
        transition: opacity .75s;
    }
    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }

    /* PRÉSENTATION */
    img.photo-character
    {
        padding:12px;height:165px; width:auto;
    }

    /*APTITUDES*/
    .row .skills
    {
        margin-bottom: 21px;
    }

    .glob-top
    {
        border: 3px solid;
        border-color: red red transparent red;
        border-radius: 8px 8px 0 0;
    }
    .glob-bot
    {
        border: 3px solid;
        border-color: transparent blue blue blue;
        border-radius: 0 0 8px 8px;
    }

    #capacity-text
    {
        font-size:13px;
        line-height:11pt;
    }

    div.left-content
    {
        border-right: 1px solid #eee;
    }

    /* OBJETS */
    div.object-card
    {
        height:45px;
        margin-left:2px;
        padding:10px;
    }

    #clue-token-img
    {
        height:20px;
        width:auto;
    }

    /* ANCIEN */
    img.destiny-token
    {
        height: 35px;
        width: 35px;
        border-radius:50%;
        display: inline-block;
        position: absolute;
        top:0;
        left:0;
    }

    div.ancient-number-ladder
    {
        height: 35px;
        width: 35px;
        border-radius:50%;
        display: inline-block;
        position: relative;
        margin-bottom:15px;
        padding-top:5px;
    }

    /* GENERAL */
    .lh-15
    {
        line-height:15pt;
    }

    .mt-25
    {
        margin-top: 25px;
    }

    .mt-5
    {
        margin-top: 5px;
    }

    hr
    {
        margin-top: 10px;
        margin-bottom: 10px;
    }

    div.justified-text
    {
        text-align:justify;
    }

    b.bold
    {
        font-weight: 900;
    }

</style>
