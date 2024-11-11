import streamlit as st
import torch
import GPUtil
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import threading

class GPUStreamlitMonitor:
    def __init__(self):
        # Configuration initiale Streamlit
        st.set_page_config(
            page_title="Monitoring GPU",
            page_icon="🖥️",
            layout="wide"
        )
        
        # Initialisation des données
        self.gpu_data = {
            'timestamp': [],
            'gpu_usage': [],
            'memory_usage': [],
            'temperature': [],
            'power_consumption': []
        }
        
        # Indicateurs de monitoring
        self.is_monitoring = False
        self.monitoring_thread = None
        
    def get_gpu_metrics(self):
        try:
            gpus = GPUtil.getGPUs()
            if not gpus:
                return None
            
            gpu = gpus[0]  # Premier GPU
            return {
                'timestamp': time.time(),
                'gpu_usage': gpu.load * 100,
                'memory_usage': gpu.memoryUsed / gpu.memoryTotal * 100,
                'temperature': gpu.temperature,
                'power_consumption': self._get_power_consumption()
            }
        except Exception as e:
            st.error(f"Erreur de récupération GPU: {e}")
            return None

    def _get_power_consumption(self):
        try:
            import pynvml
            pynvml.nvmlInit()
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            return pynvml.nvmlDeviceGetEnforcedPowerLimit(handle) / 1000  # en Watts
        except:
            return 0

    def monitoring_loop(self, duration, interval):
        start_time = time.time()
        
        while self.is_monitoring and (time.time() - start_time) < duration:
            metrics = self.get_gpu_metrics()
            
            if metrics:
                for key in self.gpu_data.keys():
                    self.gpu_data[key].append(metrics[key])
            
            time.sleep(interval)
        
        self.is_monitoring = False

    def start_monitoring(self, duration, interval):
        self.is_monitoring = True
        self.monitoring_thread = threading.Thread(
            target=self.monitoring_loop, 
            args=(duration, interval)
        )
        self.monitoring_thread.start()

    def plot_metrics(self):
        # Conversion en DataFrame
        df = pd.DataFrame(self.gpu_data)
        
        # Création de graphiques
        col1, col2 = st.columns(2)
        
        with col1:
            # Utilisation GPU
            fig_gpu = px.line(
                df, x='timestamp', y='gpu_usage', 
                title='Utilisation GPU (%)',
                labels={'gpu_usage': 'Utilisation', 'timestamp': 'Temps'}
            )
            st.plotly_chart(fig_gpu)
        
        with col2:
            # Utilisation Mémoire
            fig_memory = px.line(
                df, x='timestamp', y='memory_usage', 
                title='Utilisation Mémoire (%)',
                labels={'memory_usage': 'Mémoire', 'timestamp': 'Temps'}
            )
            st.plotly_chart(fig_memory)
        
        # Température et Consommation
        col3, col4 = st.columns(2)
        
        with col3:
            fig_temp = px.line(
                df, x='timestamp', y='temperature', 
                title='Température GPU (°C)',
                labels={'temperature': 'Température', 'timestamp': 'Temps'}
            )
            st.plotly_chart(fig_temp)
        
        with col4:
            fig_power = px.line(
                df, x='timestamp', y='power_consumption', 
                title='Consommation Électrique (W)',
                labels={'power_consumption': 'Watts', 'timestamp': 'Temps'}
            )
            st.plotly_chart(fig_power)
        
        # Statistiques résumées
        st.subheader("Statistiques GPU")
        col_stats1, col_stats2 = st.columns(2)
        
        with col_stats1:
            st.metric("Utilisation Moyenne GPU", f"{df['gpu_usage'].mean():.2f}%")
            st.metric("Utilisation Max GPU", f"{df['gpu_usage'].max():.2f}%")
        
        with col_stats2:
            st.metric("Température Max", f"{df['temperature'].max():.2f}°C")
            st.metric("Consommation Moyenne", f"{df['power_consumption'].mean():.2f} W")

    def run(self):
        st.title("🖥️ Monitoring Temps Réel GPU")
        
        # Paramètres de monitoring
        col_duration, col_interval = st.columns(2)
        
        with col_duration:
            duration = st.slider(
                "Durée du monitoring", 
                min_value=10, 
                max_value=600, 
                value=60
            )
        
        with col_interval:
            interval = st.slider(
                "Intervalle de mesure (sec)", 
                min_value=1, 
                max_value=10, 
                value=1
            )
        
        # Bouton de démarrage
        if st.button("Démarrer Monitoring"):
            # Réinitialisation des données
            for key in self.gpu_data:
                self.gpu_data[key] = []
            
            # Lancement du monitoring
            self.start_monitoring(duration, interval)
            
            # Attente de la fin du monitoring
            while self.is_monitoring:
                time.sleep(1)
            
            # Affichage des graphiques
            self.plot_metrics()

# Lancement de l'application
def main():
    monitor = GPUStreamlitMonitor()
    monitor.run()

if __name__ == "__main__":
    main()
