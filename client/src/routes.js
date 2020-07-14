// Settings
import Home from './components/settings/Home.vue';
import ChoosePlayers from './components/settings/ChoosePlayers.vue';
import ChooseCharacters from './components/settings/ChooseCharacters.vue';
import MixAllyPackage from './components/settings/MixAllyPackage.vue';
import MixInvestigatorPackage from './components/settings/MixInvestigatorPackage.vue';
import ChooseAncient from './components/settings/ChooseAncient.vue';
import SetClues from './components/settings/SetClues.vue';
import SetFixedObjects from './components/settings/SetFixedObjects.vue';
import SetRandomObjects from './components/settings/SetRandomObjects.vue';
import SetHealthSanity from './components/settings/SetHealthSanity.vue';
import SetProperties from './components/settings/SetProperties.vue';
import SetUpMonsters from './components/settings/SetUpMonsters.vue';
import MixAncientPackage from './components/settings/MixAncientPackage.vue';
import PlaceInvestigators from './components/settings/PlaceInvestigators.vue';

// Phases de tours
import MythStep from './components/mythStep/MythStep.vue';
import UpkeepStep from './components/upkeepStep/UpkeepStep.vue';
import MoveStep from './components/moveStep/MoveStep.vue';
import ArkhamEncounterStep from './components/arkhamEncounterStep/ArkhamEncounterStep.vue';
import BeyondEncounterStep from './components/beyondEncounterStep/BeyondEncounterStep.vue';

const Routes = [
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
];

export default Routes;
