import { createStore } from 'vuex'
import { subjectService } from './apiservices'
export default createStore({
    state: {
        subjects: [],
        isLoading: false,
        message: { text: "", type: "primary" },
        subjectToEdit: null,

    },
    getters: {
        allSubjects: (state) => state.subjects,
        isLoading: (state) => state.isLoading,
        message: (state) => state.message,
        subjectToEdit: (state) => state.subjectToEdit,
    },
    mutations:{
        SET_LOADING(state, isLoading) {
            state.isLoading = isLoading;
        },
        SET_SUBJECTS(state, subjects) {
            state.subjects = subjects;
        },
        ADD_SUBJECT(state, newSubject) {
            state.subjects.push(newSubject);
        },
        UPDATE_SUBJECT_IN_LIST(state, updatedSubject) {
            const index = state.subjects.findIndex(s => s.id === updatedSubject.id);
            if (index !== -1) {
                state.subjects.splice(index, 1, updatedSubject);
            }
        },
        REMOVE_SUBJECT(state, subjectId) {
            state.subjects = state.subjects.filter(s => s.id !== subjectId);
        },
        SET_MESSAGE(state, { text, type = 'success' }) {
            state.message = { text, type };
        },
        CLEAR_MESSAGE(state) {
            state.message = { text: "", type: "primary" };
        },
        SET_SUBJECT_TO_EDIT(state, subject) {
            state.subjectToEdit = subject;
        }
    },
    actions:{
        displayMessage({ commit }, { text, type, duration = 3000 }) {
            commit('SET_MESSAGE', { text, type });
            setTimeout(() => {
                commit('CLEAR_MESSAGE');
            }, duration);
        },

        async fetchSubjects({ commit }) {
            
            try {
                const subjects = await subjectService.getAll();
                commit('SET_SUBJECTS', subjects);
            } catch (error) {
                commit('SET_MESSAGE', { text: `Error fetching subjects: ${error.message}`, type: 'danger' });
            } 
        },

        async createSubject({ commit, dispatch }, formData) {
            
            try {
                const newSubject = await subjectService.create(formData);
                commit('ADD_SUBJECT', newSubject); 
                dispatch('displayMessage', { text: `Subject "${newSubject.name}" created!` });
                return Promise.resolve(newSubject);
            } catch (error) {
                dispatch('displayMessage', { text: `Error: ${error.message}`, type: 'danger' });
                return Promise.reject(error);
            } finally {
                commit('SET_LOADING', false);
            }
        },
        async updateSubject({ commit, dispatch }, subjectData) {
            commit('SET_LOADING', true);
            try {
                const updatedSubject = await subjectService.update(subjectData.id, subjectData);
                commit('UPDATE_SUBJECT_IN_LIST', updatedSubject);
                dispatch('displayMessage', { text: `Subject "${updatedSubject.name}" updated successfully!` });
                return Promise.resolve(updatedSubject);
            } catch (error) {
                dispatch('displayMessage', { text: `Error: ${error.message}`, type: 'danger' });
                return Promise.reject(error);
            } finally {
                commit('SET_LOADING', false);
            }
        },

        async deleteSubject({ commit, dispatch }, subjectId) {
            // if (!confirm("Are you sure you want to delete this subject?")) return;
            
            commit('SET_LOADING', true)
            try {
                await subjectService.delete(subjectId);
                commit('REMOVE_SUBJECT', subjectId);
                dispatch('displayMessage', { text: "Subject deleted successfully." });
            } catch (error) {
                dispatch('displayMessage', { text: `Error deleting subject: ${error.message}`, type: 'danger' });
            } finally {
                commit('SET_LOADING', false);
            }
        },
    } ,
    
})