<template>
    <div v-if="isModalOpen" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(5px); z-index: 999;">
    </div>

    <div v-if="isModalOpen" style="position: fixed; top: 20%; left: 50%; transform: translateX(-50%); z-index: 1000; width: 400px;">
        <v-card>
            <v-card-title>
                {{ isEditing ? 'Edit User' : 'Create User' }}
            </v-card-title>
            <v-card-text>
                <v-form ref="form" @submit.prevent="validateAndSave">
                    <v-text-field v-model="form.username" label="Username" :rules="usernameRules" required></v-text-field>
                    <v-text-field v-model="form.password" label="Password" type="password" :rules="usernameRules" required></v-text-field>
                    <v-select v-model="form.roles" :items="['admin', 'manager', 'tester']" label="Roles" multiple required></v-select>
                    <v-text-field v-model="form.timezone" label="Timezone" required></v-text-field>
                    <v-checkbox v-model="form.active" label="Is Active?"></v-checkbox>
                    <v-btn type="submit" color="primary">Save</v-btn>
                    <v-btn @click="$emit('close')">Cancel</v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
export default {
    props: {
        isModalOpen: Boolean,
        isEditing: Boolean,
        form: Object,
    },
    emits: ['update:isModalOpen', 'save', 'close'],
    data() {
        return {
            usernameRules: [
                v => !!v || 'Username is required',
                v => (v && v.trim().length > 0) || 'Username cannot be empty',
            ],
            passwordRules: [
                v => !!v || 'Password is required',
                v => (v && v.trim().length > 0) || 'Password cannot be empty',
            ],
        }
    },
    methods: {
        validateAndSave() {
            const isFormValid = this.$refs.form.validate();
            if (isFormValid) {
                this.$emit('save');
            } else {
                console.error('Form validation failed');
            }
        },
        validateForm() {
            return this.$refs.form.validate();
        },
        closeModal() {
            this.$emit('close')
        },
    },
};
</script>
