import { registerPlugins } from '@/plugins'
import App from './App.vue'
import { createApp } from 'vue'
import axios from './plugins/api';
import 'vuetify/styles';

const app = createApp(App)
app.config.globalProperties.$axios = axios;
registerPlugins(app)
app.mount('#app');
