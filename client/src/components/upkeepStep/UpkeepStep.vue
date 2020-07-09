<template>
        <body>
            <app-sidebar></app-sidebar>

            <!-- ARKHAM MAP -->
            <app-map :investigators="investigators"
                     :sites="sites"
                     :beyond="beyond"
                     :specials="specials"
                     :monsters="monsters"
                     :objects="objects"
                     @wasClicked="setNewSite($event)"
                     ref="appmap"></app-map>

            <!-- Modales d'entretien -->

            <!-- Modale d'entretien -->
            <div id="modal-upkeep"  v-if="upkeepStep!=1" class="modal open center-align" tabindex="0">
                <div class="modal-content" style="height:100%;">
                    <h4 class="">Phase d'entretien</h4><br>

                    <!-- Affichage des personnages qui ne seront pas concernés par l'entretien -->
                    <transition name="fade" mode="out-in">
                        <div v-if="upkeepStep==0" key="0">
                            <p>Les joueurs qui ont été arrêtés, perdus dans le Temps et l’Espace ou qui passent leur tour au tour précédent ne sont pas concernés par la phase d’entretien.</p>
                            <ul>
                                <!-- Affichage du status des investigateurs mis de côté -->
                                <li v-for="investigator of investigators" v-if="investigator.status !='ok'" class="">
                                    <span >{{ investigator.name }} est
                                        <span v-if="investigator.status=='lost'">perdu(e) dans le temps et l'espace</span>
                                        <span v-if="investigator.status=='arrested'">arrêté(e)</span>
                                        <span v-if="investigator.status=='retarded'">retardé(e)</span>
                                    </span>
                                </li>
                            </ul>
                        </div>
                        <!-- <div v-if="upkeepStep==1" key="1">
                            <p>Les investigateurs perdus dans le Temps et l’Espace se déplacent sur le lieu d’Arkham de leur choix.</p>
                        </div> -->
                        <div v-if="upkeepStep==2" key="2">
                            <p>Restauration des cartes déchargées.</p>
                        </div>
                        <div v-if="upkeepStep==3" key="3">
                            <p>Résolutions des actions d'entretien (vérification des bénédictions/malédictions, acompte, prêts bancaires, ...)</p>
                        </div>
                        <div v-if="upkeepStep==4" key="4">
                          <p>Ajustement de vos compétences en fonction de la valeur de Concentration.</p>
                        </div>
                    </transition>

                    <button class="btn waves-effect waves-light teal right-align right" @click="nextUpkeepStep">ok</button>
                </div>
            </div>

            <!-- Modale d'entretien -->
            <div id="modal-upkeep-1" v-if="upkeepStep==1" class="modal open" tabindex="0">
                <div class="modal-content" style="height:100%;">
                    <h4>Phase d'entretien</h4><br>

                    <!-- Affichage des personnages qui ne seront pas concernés par l'entretien -->
                    <p>Les investigateurs perdus dans le Temps et l’Espace se déplacent sur le lieu d’Arkham de leur choix.</p>
                    <p>Choisir un lieu pour :</p>
                        <!-- Affichage du status des investigateurs mis de côté -->

                        <div v-for="(investigator, index) of lostInvestigators">

                            <button class="waves-effect waves-light btn-small teal btn-investigator"
                                v-if="investigator.visible == true"
                                :disabled="(current!=index)&&(next==false)"
                                @click="resetSite(index)"
                                v-html="investigator.name">
                                </button>
                            <blockquote v-if="investigator.newSiteName !=''">
                                <span  class=""
                                       v-html="investigator.newSiteNameText"></span>
                            </blockquote>
                        </div>
                        <br>
                        <div class="modal-footer right-align">

                            <button class="btn waves-effect waves-light teal "
                                style=" display: inline-block;"
                                :disabled="next == false"
                                @click="nextUpkeepStep">
                                valider les déplacements
                            </button>
                        </div>
                </div>
            </div>
        </body>

</template>

<script>
import Sidebar from '../Sidebar.vue';
import Map from '../Map.vue';

export default {
  // déclaration des composants utilisés
  components: {
    'app-sidebar': Sidebar,
    'app-map': Map,
  },
  data() {
    return {
      pageTitle: 'Phase d\'entretien',
      playerNumber: 4,
      current: 0,
      next: false,
      upkeepStep: 0,
      lostInvestigators: [],
      lastClicked: '',
      investigators: [
        {
          id: 1, name: 'Joe Diamond', siteId: 3, status: 'ok',
        },
        {
          id: 2, name: 'Francis Sailor', siteId: 36, status: 'lost',
        },
        {
          id: 3, name: 'Jenny Barnes', siteId: 9, status: 'arrested',
        },
        {
          id: 4, name: 'Peggy Green', siteId: 6, status: 'retarded',
        },
        {
          id: 5, name: 'Mark Harrigan', siteId: 36, status: 'lost',
        },
      ],
      objects: [
        {
          id: 1,
          nom: 'Lance-flamme',
          status: false,
        },
      ],
      monsters: [
        {
          id: 1, name: 'Chthonien', siteId: 11, symbol: 'triangle', habilities: {},
        },
        {
          id: 2, name: 'Migo', siteId: 1, symbol: 'cercle', habilities: {},
        },
        {
          id: 3, name: 'Cultiste', siteId: 3, symbol: 'lune', habilities: {},
        },
      ],
      sites: [
        {
          name: 'Boutique<br>de<br>souvenir', id: '1', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: 'Journal', id: '2', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: 'Gare', id: '3', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 27, black: 27,
        },
        {
          name: "Banque<br>d'Arkham", id: '4', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: "Asile<br>d'Arkham", id: '5', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: "Square de<br>l'indépen-<br>-dance", id: '6', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'white', portal: [], marker: [], white: 28, black: 28,
        },
        {
          name: 'Relais<br>routier<br>de Hibb', id: '7', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: 'Restaurant<br>de Velma', id: '8', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: 'Poste<br>de<br>-police', id: '9', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'grey', portal: [], marker: [], white: 29, black: 29,
        },
        {
          name: "L'ile<br>inexplorée", id: '10', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: 'Les<br>quais', id: '11', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: "l'Inno-<br>-mable", id: '12', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'green', portal: [], marker: [], white: 30, black: 30,
        },
        {
          name: 'Le<br>cimetière', id: '13', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'La Caverne<br>noire', id: '14', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'Le<br>magasin', id: '15', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'purple', portal: [], marker: [], white: 31, black: 31,
        },
        {
          name: 'Département<br>Scientifique', id: '16', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Adminis-<br>-tration', id: '17', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Biblio-<br>-thèque', id: '18', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 32, black: 32,
        },
        {
          name: 'Maison<br>de la<br>sorcière', id: '19', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'blue', portal: [], marker: [], white: 33, black: 33,
        },
        {
          name: "Loge du<br>crépuscule<br>d'argent", id: '20', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'blue', portal: [], marker: [], white: 33, black: 33,
        },
        {
          name: 'Hôpital<br>Sainte<br>Marie', id: '21', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Vieille<br>échoppe<br>de magie', id: '22', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Les<br>bois', id: '23', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'red', portal: [], marker: [], white: 34, black: 34,
        },
        {
          name: 'Pension<br>de Ma', id: '24', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Société<br>des<br>historiens', id: '25', type: 'site', character: [], monster: [], event: [], clue: 1, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        {
          name: 'Eglise<br>méridionale', id: '26', type: 'site', character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 35, black: 35,
        },
        /* 'Migo' */ {
          name: 'Quartier<br>Nord', id: '27', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'orange', portal: [], marker: [], white: 28, black: 30,
        },
        /* 'Cultiste' */ {
          name: 'Centre<br>Ville', id: '28', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'white', portal: [], marker: [], white: 29, black: 27,
        },
        {
          name: 'Quartier<br>Est', id: '29', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'grey', portal: [], marker: [], white: 31, black: 28,
        },
        {
          name: 'Quartier<br>marchand', id: '30', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'green', portal: [], marker: [], white: 27, black: 32,
        },
        {
          name: 'Quartier<br>de la<br>rivière', id: '31', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'purple', portal: [], marker: [], white: 33, black: 29,
        },
        {
          name: 'Université<br>Miskatonik', id: '32', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'yellow', portal: [], marker: [], white: 30, black: 34,
        },
        {
          name: 'French<br>Hill', id: '33', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'blue', portal: [], marker: [], white: 35, black: 31,
        },
        {
          name: 'Quartier<br>Résidentiel', id: '34', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'red', portal: [], marker: [], white: 32, black: 35,
        },
        {
          name: 'Quartier<br>sud', id: '35', type: 'street', character: [], monster: [], event: [], clue: 0, color: 'brown', portal: [], marker: [], white: 34, black: 33,
        },

      ],
      beyond: [
        {
          id: 1,
          name: 'Une autre<br>dimension',
          colors: [],
          steps: [
            {
              id: 1, position: 1, character: [], monster: [],
            },
            {
              id: 2, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 2,
          name: 'Les Abysses',
          colors: [],
          steps: [
            {
              id: 3, position: 1, character: [], monster: [],
            },
            {
              id: 4, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 3,
          name: 'Cité de la<br>Grand Race',
          colors: [],
          steps: [
            {
              id: 5, position: 1, character: [], monster: [],
            },
            {
              id: 6, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 4,
          name: 'Yuggoth',
          colors: [],
          steps: [
            {
              id: 7, position: 1, character: [], monster: [],
            },
            {
              id: 8, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 5,
          name: 'Grand Hall<br>de Celeano',
          colors: [],
          steps: [
            {
              id: 9, position: 1, character: [], monster: [],
            },
            {
              id: 10, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 6,
          name: 'Les contrées<br>du rêve',
          colors: [],
          steps: [
            {
              id: 11, position: 1, character: [], monster: [],
            },
            {
              id: 12, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 7,
          name: 'Plateau<br>de Leng',
          colors: [],
          steps: [
            {
              id: 13, position: 1, character: [], monster: [],
            },
            {
              id: 14, position: 2, character: [], monster: [],
            },
          ],
        },
        {
          id: 8,
          name: 'R\'lyeh',
          colors: [],
          steps: [
            {
              id: 15, position: 1, character: [], monster: [],
            },
            {
              id: 16, position: 2, character: [], monster: [],
            },
          ],
        },
      ],
      specials: [
        { name: 'Perdu dans<br>le temps<br>et l\'espace', id: 36, character: [{ id: 2, name: 'Francis Sailor' }, { id: 5, name: 'Mark Harrigan' }] },
        { name: 'Ciel', id: 37, monster: [] },
        { name: 'Périphérie', id: 38, monster: [] },
        { name: 'Cellule de prison', id: 39, monster: [] },
      ],

    };
  },
  methods: {
    nextUpkeepStep() {
      if (this.upkeepStep < 5) {
        this.upkeepStep++;
        switch (this.upkeepStep) {
          case 2:
            // Début de phase de rechargement des cartes (donc prise en compte du mouvement des investigateurs qui sortent de perdu dans le temps et l'espace)
            // Modification de site des investigateurs perdus dans le temps et l'espace
            this.lostInvestigators.forEach((lost) => {
              // on recherche le personnage avec l'id en cours
              const updatedCharacter = this.getInvestigator(lost.id);
              // Enregistremet de l'id de l'ancien site
              const oldSite = updatedCharacter.siteId;
              // On donne au personnage en cours le nouveau site et on redéfinit son statut à ok
              updatedCharacter.siteId = lost.newSiteId;
              updatedCharacter.status = 'ok';
              // vide des joueurs perdus dans le temps et l'espace
              // Reste à vérifier si l'on ne perd pas des joueurs qui devraient y rester : voir s'il y a des règles qui font que certains devraient rester
              this.deleteLost(updatedCharacter.id);
            });
            this.$refs.appmap.updateMap();
            // Rechargement de tous les objets
            this.objects.forEach((object) => {
              object.status = true;
            });
            break;
          case 3:
            // activation des actions d'entretien
            console.log("actions d'entretien");
            break;
          case 5:
            // activation des actions d'entretien
            console.log("actions d'entretien");
            this.$router.push('move-step');
            break;
        }
      }
    },
    // Récupère l'investigateur dont l'id est passé en paramètre
    getInvestigator(id) {
      return this.investigators.find(investigator => investigator.id == id);
    },
    // Supression de l'investigateur dont l'id est en paramètres de "perdu dans le temps et l'espace"
    deleteLost(id) {
      // pour chaque investigateur perdu dans le temps et l'espace
      this.specials[0].character.forEach((char, index) => {
        // si son id est celui recherché, on le supprime du lieu perdu dans le temps et l'espace
        if (char.id == id) this.specials[0].character.splice(index, 1);
      });
    },
    // Définit un nouveau site, appelé au clique sur un site
    setNewSite(data) {
      if (this.upkeepStep == 1) {
        // On définit le dernier site cliqué
        this.lastClicked = data;
        // définition du personage en cours
        const currentCharacter = this.lostInvestigators[this.current];
        // définition du nouveau site
        currentCharacter.newSiteId = this.lastClicked.id;
        currentCharacter.newSiteName = this.lastClicked.name;
        currentCharacter.newSiteNameText = this.lastClicked.name.replace('-<br>-', '').replace('<br>', ' ');

        // Prochain joueur
        this.nextCurrent();
      }
    },
    nextCurrent() {
      // Si le joueur actuel n'est pas le dernier
      if ((this.current + 1) < this.lostInvestigators.length) {
        // Joueur suivant et apparition de son bouton
        this.current++;
        this.lostInvestigators[this.current].visible = true;
      }
      // Sinon apparition du bouton etape suivante
      else if ((this.current + 1) == this.lostInvestigators.length) {
        this.next = true;
      }
    },
    resetSite(id) {
      // changement du joueur en cours et reset de ses valeurs newsite
      this.current = id;
      this.lostInvestigators[this.current].newSiteId = '';
      this.lostInvestigators[this.current].newSiteName = '';
      this.lostInvestigators[this.current].newSiteNameText = '';
      this.next = false;
    },
    log(message) {
      console.log(message);
    },

    continueAction() {
      console.log('ici');
      // this.$router.push('choose-ancient')
    },
  },
  updated() {
  },
  mounted() {
    // On récupère les investigateurs perdus dans le temps et l'espace
    this.investigators.forEach((investigator) => {
      if (investigator.status == 'lost') this.lostInvestigators.push(investigator);
    });
    this.lostInvestigators.forEach((lost, index) => {
      // On ne rend visible que le bouton du premier
      if (index == 0) lost.visible = true;
      else lost.visible = false;
    });
  },
};
</script>

<style>
    /*TRANSITIONS*/
    .fade-enter-active, .fade-leave-active {
        transition: opacity .75s;
    }
    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }

    /*Modales*/
    #modal-upkeep
    {
        z-index: 1003;
        display: block;
        opacity: 1;
        top: 10%;
        transform: scaleX(1) scaleY(1);
        height:450px;
    }

    #modal-upkeep-1
    {
        width: 20%;
        top: 10%;
        margin-left: 25px;
        z-index: 1003;
        display: block;
        opacity: 1;
        height:100%;
    }
    .btn
    {
        margin: 2px;
    }
    .btn-investigator
    {
        margin: 5px;
    }

</style>
