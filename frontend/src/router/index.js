import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/pages/index.vue';
import UserPage from '@/pages/UserPage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/user/:id',
      name: 'User page',
      component: UserPage,
    }
  ],
});

export default router;

