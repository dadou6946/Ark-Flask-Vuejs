import Vue from 'vue';
import VueRouter from 'vue-router';

import App from './views/App';

// Settings
import Home from './components/settings/Home';
import ChoosePlayers from './components/settings/ChoosePlayers';
import ChooseCharacters from './components/settings/ChooseCharacters';
import MixAllyPackage from './components/settings/MixAllyPackage';
import MixInvestigatorPackage from './components/settings/MixInvestigatorPackage';
import ChooseAncient from './components/settings/ChooseAncient';
import SetClues from './components/settings/SetClues';
import SetFixedObjects from './components/settings/SetFixedObjects';
import SetRandomObjects from './components/settings/SetRandomObjects';
import SetHealthSanity from './components/settings/SetHealthSanity';
import SetProperties from './components/settings/SetProperties';
import SetUpMonsters from './components/settings/SetUpMonsters';
import MixAncientPackage from './components/settings/MixAncientPackage';
import PlaceInvestigators from './components/settings/PlaceInvestigators';

// Phases de tours
import MythStep from './components/mythStep/MythStep';
import UpkeepStep from './components/upkeepStep/UpkeepStep';
import MoveStep from './components/moveStep/MoveStep';
import ArkhamEncounterStep from './components/arkhamEncounterStep/ArkhamEncounterStep';
import BeyondEncounterStep from './components/beyondEncounterStep/BeyondEncounterStep';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/choose-characters',
      name: 'choose-characters',
      component: ChooseCharacters,
    },
    {
      path: '/choose-players',
      name: 'choose-players',
      component: ChoosePlayers,
    },
    {
      path: '/choose-ancient',
      name: 'choose-ancient',
      component: ChooseAncient,
    },
    {
      path: '/mix-ally-package',
      name: 'mix-ally-package',
      component: MixAllyPackage,
    },
    {
      path: '/set-clues',
      name: 'set-clues',
      component: SetClues,
    },
    {
      path: '/set-fixed-objects',
      name: 'set-fixed-objects',
      component: SetFixedObjects,
    },
    {
      path: '/mix-investigator-package',
      name: 'mix-investigator-package',
      component: MixInvestigatorPackage,
    },
    {
      path: '/set-random-objects',
      name: 'set-random-objects',
      component: SetRandomObjects,
    },
    {
      path: '/set-health-sanity',
      name: 'set-health-sanity',
      component: SetHealthSanity,
    },
    {
      path: '/set-properties',
      name: 'set-properties',
      component: SetProperties,
    },
    {
      path: '/set-up-monsters',
      name: 'set-up-monsters',
      component: SetUpMonsters,
    },
    {
      path: '/mix-ancient-package',
      name: 'mix-ancient-package',
      component: MixAncientPackage,
    },
    {
      path: '/place-investigators',
      name: 'place-investigators',
      component: PlaceInvestigators,
    },
    {
      path: '/myth-step',
      name: 'myth-step',
      component: MythStep,
    },
    {
      path: '/upkeep-step',
      name: 'upkeep-step',
      component: UpkeepStep,
    },
    {
      path: '/move-step',
      name: 'move-step',
      component: MoveStep,
    },
    {
      path: '/arkham-encounter-step',
      name: 'arkham-encounter-step',
      component: ArkhamEncounterStep,
    },
    {
      path: '/beyond-encounter-step',
      name: 'beyond-encounter-step',
      component: BeyondEncounterStep,
    },

  ],
});

const app = new Vue({
  el: '#app',
  components: { App },
  router,
});
