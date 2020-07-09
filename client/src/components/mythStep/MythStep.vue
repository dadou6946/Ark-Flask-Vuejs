<template>
        <body>
            <app-sidebar></app-sidebar>

            <!-- ARKHAM MAP -->
            <app-map :investigators="investigators"
                     :sites="sites"
                     :beyond="beyond"
                     :specials="specials"
                     :monsters="monsters"></app-map>

            <!-- Modales de mythe -->

            <!-- Modale d'appercu de carte -->
            <div id="modal-myth-1" class="modal" tabindex="0">
                <div class="modal-content" style="height:100%">
                    <div class="row">
                        <div class="col s12">

                            <h4>Phase de mythe</h4><br>
                            <div>On pioche une carte mythe</div><br><br>
                            <!-- Image de la carte à trouver -->
                            <transition name="fade">
                                <img class="responsive-img"
                                    src="/image/card/myth/Astres_Propices.jpg"
                                    alt="Astres_Propices"
                                    v-if="!hide.mythImage"
                                    v-bind:style="{ width: '100%' }"/>
                            </transition>

                        </div>
                    </div>
                </div>
            </div>

            <!-- Modale des étapes de mythe -->
            <div id="modal-myth-2" class="modal open modal-fixed-footer right" tabindex="0">
                <div class="modal-content" style="height:100%">
                    <div class="row">

                        <div class="col s12">
                            <ul class="collection" v-if="mythStep>0">
                                <!-- APPARITION DU PORTAIL -->
                                <li class="collection-item" v-if="mythStep>=1">
                                    <span v-if="mythResume.portal.action=='add'">Un portail vers <span v-html="mythResume.portal.portalName"></span> apparaît à/au : <span v-html="mythResume.portal.siteName"></span>.</span>
                                    <span v-if="mythResume.portal.action=='already'">Un portail devrait apparaître à/au <span v-html="mythResume.portal.siteName"></span> mais il y en a déjà un!</span>
                                    <span v-if="mythResume.portal.action=='none'">Un portail devrait apparaître à/au <span v-html="mythResume.portal.siteName"></span> mais il y a un Signe des Anciens. Aucun portail n'apparaît.</span>
                                </li>
                                <!-- ARRIVEE DU MONSTRE -->
                                <li class="collection-item" v-if="mythStep>=2">
                                    <span v-if="mythResume.monster.action=='add'">Un monstre apparaît au même lieu.<br>C'est un(e) <span v-html="mythResume.monster.monsterName"></span>.</span>
                                    <span v-if="mythResume.monster.action=='wave'">Une vague de montres se produit.</span>
                                    <span v-if="mythResume.monster.action=='none'">Aucun monstre n'apparaît.</span>
                                </li>
                                <!-- INDICE -->
                                <li class="collection-item" v-if="mythStep>=3">
                                    <span v-if="mythResume.clue.action=='add'">Un indice apparaît à : <br><span v-html="mythResume.clue.siteName"></span></span>
                                    <span v-if="mythResume.clue.action=='none'">
                                        Un indice devrait apparaître à :  <span v-html="mythResume.clue.siteName"></span>.<br>
                                        Mais un portail y est ouvert. Il n'est pas ajouté.
                                    </span>
                                </li>
                                <!-- DEPLACEMENT DES MONSTRES -->
                                <li class="collection-item" v-if="mythStep>=4">
                                    Les monstres se déplacent :
                                    <ul>
                                        <li>-
                                            <span v-for="(symbol, index) of mythResume.move.white">
                                                <span v-html="symbol"></span>
                                                <span v-if="index+1 < mythResume.move.white.length"> - </span>
                                            </span>
                                            <img src="https://img.icons8.com/ios/24/000000/right.png"> fleche blanche
                                        </li>
                                        <li>-
                                            <span v-for="(symbol, index) of mythResume.move.black">
                                                <span v-html="symbol"></span>
                                                <span v-if="index+1 < mythResume.move.black.length"> - </span>
                                            </span>
                                            <img src="https://img.icons8.com/ios/24/000000/right.png"> flèche noir
                                        </li>
                                    </ul>
                                </li>
                                <!-- EVENEMENT -->
                                <li class="collection-item" v-if="mythStep>=5">
                                    C'est un(e) {{ mythResume.event.action }} :<br> <strong>{{mythResume.event.name}}</strong>.<br>
                                    Lieu d'activité: {{ mythResume.event.siteName }}
                                </li>
                            </ul>
                        </div>

                    </div>
                </div>
                <div class="modal-footer">
                    <button v-bind:disabled="mythStep==5" @click="next" class="waves-effect waves-light btn-flat teal">Ok</button>
                    <button v-bind:disabled="mythStep<5" @click="continueAction" class="waves-effect waves-light btn-flat teal">Etape suivante</button>
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
      pageTitle: 'Phase de mythe',
      playerNumber: 2, // nombre de joueurs
      hide: // permet de cacher certains éléments
                    { mythImage: true },
      mythStep: 0, // phase en cours (1->apparition de portail, 2->monstre, 3->indice, 4->mouvement des monstres, 5->évènement)
      mythResume: // résumé de la carte mythe récupérée
                    {
                      // Types d'actions : add (ajout d'un portail), already (pas d'ajout: portail déja présent), none (pas d'ajout:signe anciens), terror (augmentation du niveau de terreur), destiny (augmentation de l'échelle de l'ancien)
                      // Penser que l'on peut avoir un portail qui s'ouvre même si le lieu est scellé : irruption de portail qui détruit le signe des anciens (dunwich)!
                      portal: {
                        action: 'add', portalName: 'Yuggoth', portalId: 5, siteName: "Square de l'indépendance", siteId: 6,
                      },
                      // Types d'actions : add (ajout d'un monstre), wave (vague de monstres), none (pas d'ajout:signe anciens)
                      monster: {
                        action: 'add', monsterName: 'Zombie', monsterId: 2, siteName: "Square de l'indépendance", siteId: 6,
                      },
                      // Types d'actions : add (ajout d'un indice), none (pas d'ajout:portail)
                      clue: { action: 'add', siteName: 'Boutique de souvenirs', siteId: 1 },
                      // Types d'action : simple (certains signes bougent), global(tous les signes bougent)n none (aucun)
                      move: { action: 'simple', white: ['slash', 'triangle', 'étoile'], black: ['hexagone'] },
                      // Types d'action : rumor, environment, headline (gros titre)
                      event: {
                        action: 'rumeur', eventId: 1, name: 'Les astres sont propices', siteId: 28, siteName: 'Rues du Centre Ville',
                      },
                    },
      investigators: [
        { id: 1, name: 'Joe Diamond', siteId: 3 },
        { id: 2, name: 'Francis Sailor', siteId: 1 },
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
        { name: 'Perdu dans<br>le temps<br>et l\'espace', id: 36, character: [] },
        { name: 'Ciel', id: 37, monster: [] },
        { name: 'Périphérie', id: 38, monster: [] },
        { name: 'Cellule de prison', id: 39, monster: [] },
      ],

    };
  },
  methods: {

    // Etape mythe suivante
    next() {
      if (this.mythStep < 5) this.mythStep++;

      switch (this.mythStep) {
        case 1:
          // nom de portail et id de site
          var { portalName } = this.mythResume.portal;
          var { siteId } = this.mythResume.portal;
          // Pour chacun des sites
          this.sites.forEach((site) => {
            // Si le site est celui où le portail doit apparaître
            if (site.id == siteId) {
              // On l'ajoute s'il n'y a pas déjà de portail
              if (site.portal.length == 0) site.portal.push(portalName);
              // Sinon rien, vague de monstres
              else console.log('vague de monstre');
            }
          });
          break;
        case 2:
          // Définition du nom de monstre et id de site
          var { siteId } = this.mythResume.monster;
          var { monsterName } = this.mythResume.monster;
          // Pour chaque site
          this.sites.forEach((site) => {
            // Si le site est celui où le monstre doit apparaître
            if (site.id == siteId) site.monster.push(monsterName);
          });
          break;
        case 3:
          // Définition du nom de monstre et id de site d'apparition d'indice
          var { siteId } = this.mythResume.clue;
          // Pour chaque site
          this.sites.forEach((site) => {
            // Si c'est le site d'apparition d'indice, on en ajoute un
            if (site.id == siteId) site.clue++;
          });
          break;
        case 4:
          // Pour chacun des monstres
          this.monsters.forEach((monster) => {
            // Si le symbole du monstre correspond au symbole de déplacements blanc
            if (this.mythResume.move.white.indexOf(monster.symbol) != -1) {
              // On recherche le site où se trouvait le monstre
              var oldSite = this.sites.find(site => site.id == monster.siteId);
              // Modification de la localisation du monstre
              monster.siteId = oldSite.white;
              var siteFrom = this.sites.find(site => site.id == oldSite.id);
              var index = siteFrom.monster.indexOf(monster.name);
              siteFrom.monster.splice(index, 1);
              // Modification de la map : ajout dans le nouveau site
              var siteTo = this.sites.find(site => site.id == oldSite.white);
              siteTo.monster.push(monster.name);
            }

            if (this.mythResume.move.black.indexOf(monster.symbol) != -1) {
              // On recherche le site où se trouvait le monstre
              var oldSite = this.sites.find(site => site.id == monster.siteId);
              // Modification de la localisation du monstre
              monster.siteId = oldSite.black;
              var siteFrom = this.sites.find(site => site.id == oldSite.id);
              var index = siteFrom.monster.indexOf(monster.name);
              siteFrom.monster.splice(index, 1);
              // Modification de la map : ajout dans le nouveau site
              var siteTo = this.sites.find(site => site.id == oldSite.black);
              siteTo.monster.push(monster.name);
            }
          });

          break;
        case 5:
          // Définition de l'id du site d'activité de la rumeur et de son nom
          var { siteId } = this.mythResume.event;
          var { name } = this.mythResume.event;
          // Ajout de la rumeur sur la map
          this.sites.forEach((site) => {
            if (site.id == siteId) site.event.push(name);
          });
          break;
      }
    },

    switchNavbar(libelle) {
      this.navbar[libelle] = !this.navbar[libelle];
    },
    showInvestigator(name) {
      this.investigatorPreview = name;
    },
    log(message) {
      console.log(message);
    },

    continueAction() {
      // console.log('ici')
      this.$router.push('upkeep-step');
    },
  },
  updated() {

  },
  mounted() {
    // Affichage de la carte mythe au bout d'une seconde
    setTimeout(() => {
      this.hide.mythImage = false;
      // passage à la séquence de mythe suivante
      this.next();
    }, 1000);
  },
};
</script>

<style>

    /*Modales*/
    #modal-myth-1
    {
        z-index: 999;
        display: block;
        opacity: 1;
        top: 5%;
        width: 20%;
        margin-left: 25px;
    }
    #modal-myth-2
    {
        z-index: 999;
        display: block;
        opacity: 1;
        top: 5%;
        width: 20%;
        margin-right: 25px;
        height:100%;
    }

</style>
