<template>
    <v-container>
        <v-btn color="primary" @click="goToHomePage" style="margin-bottom: 20px;">
            Return to Homepage
        </v-btn>

        <v-table>
            <thead>
                <tr>
                    <th>Username</th>
                    <th>Roles</th>
                    <th>Timezone</th>
                    <th>Is Active?</th>
                    <th>Created At</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-if="user">
                    <td>{{ user.username }}</td>
                    <td>{{ user.roles.join(', ') }}</td>
                    <td>{{ user.preferences.timezone }}</td>
                    <td>{{ user.active ? 'Yes' : 'No' }}</td>
                    <td>{{ formatDate(user.created_ts) }}</td>
                    <td>
                        <v-btn color="warning" @click="openEditModal(user)">Edit</v-btn>
                        <v-btn color="error" @click="confirmDelete(user)">Delete</v-btn>
                    </td>
                </tr>
            </tbody>
        </v-table>

        <UserModal
            :isModalOpen="isModalOpen"
            @update:isModalOpen="isModalOpen = $event"
            :isEditing="isEditing"
            :form="form"
            @save="saveUser"
            @close="closeModal"
        />

        <DeleteConfirmationModal 
            :isOpen="isDeleteDialogOpen"
            @update:isOpen="isDeleteDialogOpen = $event"
            @confirm="deleteUser"
            @close="isDeleteDialogOpen = false"
        />

    </v-container>
</template>

<script>
import UserModal from '@/components/UserModal.vue';
import DeleteConfirmationModal from '@/components/DeleteConfirmationModal.vue'

export default {
    components: {
        UserModal,
        DeleteConfirmationModal,
    },
    data() {
        return {
            user: null,
            isModalOpen: false,
            isEditing: false,
            isDeleteDialogOpen: false,
            form: {
                username: '',
                password: '',
                roles: [],
                timezone: '',
                active: true,
            },
            selectedUser: null,
        };
    },
    methods: {
        async fetchUser() {
            try {
                const userId = this.$route.params.id;
                const response = await this.$axios.get(`/${userId}`);
                this.user = response.data;
            } catch (err) {
                console.error('Error fetching user', err);
            }
        },

        openEditModal(user) {
            this.isEditing = true;
            this.selectedUser = user;
            this.form = {
                username: user.username,
                password: '',
                roles: user.roles,
                timezone: user.preferences.timezone,
                active: user.active,
            };
            this.isModalOpen = true;
        },

        closeModal() {
            this.isModalOpen = false;
        },

        async saveUser() {
            try {
                const userData = {
                    username: this.form.username,
                    password: this.form.password,
                    roles: this.form.roles,
                    preferences: {
                        timezone: this.form.timezone,
                    },
                    active: this.form.active,
                };

                const url = `/${this.selectedUser._id}`;
                await this.$axios.put(url, userData);

                this.closeModal();
                this.fetchUser();
            } catch (err) {
                console.error('Error saving user:', err);
            }
        },

        confirmDelete(user) {
            this.selectedUser = user;
            this.isDeleteDialogOpen = true;
        },

        async deleteUser() {
            try {
                await this.$axios.delete(`/${this.selectedUser._id}`);
                this.isDeleteDialogOpen = false;
                this.$router.push('/');
            } catch (err) {
                console.error('Error deleting user:', err);
            }
        },

        formatDate(timestamp) {
            if (!timestamp) return 'N/A';
            const date = new Date(timestamp * 1000);
            return date.toLocaleString();
        },

        goToHomePage() {
            this.$router.push('/')
        },
    },
    mounted() {
        this.fetchUser();
    },
};
</script>
