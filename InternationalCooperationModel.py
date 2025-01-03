import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class InternationalCooperationModel:
    def __init__(self):
        # Model parameters
        self.tech_transfer_rate = 0.3
        self.trade_growth_rate = 0.2
        self.collaboration_factor = 0.4
        self.resource_constraint = 0.1
        
    def cooperation_dynamics(self, state, t, a, b, c, d):
        """
        Model dynamics for international cooperation
        state[0]: Economic development level region 1
        state[1]: Economic development level region 2
        """
        region1, region2 = state
        
        # Positive feedback loops
        d_region1 = (a * region1 * (1 - region1/100) + 
                    b * region1 * region2 / (1 + region2))
        
        d_region2 = (c * region2 * (1 - region2/100) + 
                    d * region1 * region2 / (1 + region1))
        
        return [d_region1, d_region2]
    
    def simulate_cooperation(self, years=50):
        """Simulate cooperation development over time"""
        # Time points
        t = np.linspace(0, years, years*12)
        
        # Initial conditions
        initial_state = [20, 20]  # Starting development levels
        
        # Parameters
        params = (self.tech_transfer_rate, 
                 self.trade_growth_rate,
                 self.collaboration_factor,
                 self.resource_constraint)
        
        # Solve ODE
        solution = odeint(self.cooperation_dynamics, 
                         initial_state, t, 
                         args=params)
        
        return t, solution
    
    def calculate_metrics(self, solution):
        """Calculate cooperation metrics"""
        region1_final = solution[-1, 0]
        region2_final = solution[-1, 1]
        
        total_growth = np.sum(solution[-1]) - np.sum(solution[0])
        synergy_index = (solution[-1, 0] * solution[-1, 1]) / \
                       (solution[0, 0] * solution[0, 1])
        
        return {
            'Region 1 Final Level': region1_final,
            'Region 2 Final Level': region2_final,
            'Total Growth': total_growth,
            'Synergy Index': synergy_index
        }
    
    def plot_results(self, t, solution):
        """Plot simulation results"""
        plt.figure(figsize=(12, 8))
        
        # Development levels over time
        plt.subplot(2, 1, 1)
        plt.plot(t, solution[:, 0], 'b-', label='Region 1')
        plt.plot(t, solution[:, 1], 'g-', label='Region 2')
        plt.xlabel('Time (Years)')
        plt.ylabel('Development Level')
        plt.title('Regional Development Through Cooperation')
        plt.legend()
        plt.grid(True)
        
        # Phase space
        plt.subplot(2, 1, 2)
        plt.plot(solution[:, 0], solution[:, 1], 'r-')
        plt.xlabel('Region 1 Development')
        plt.ylabel('Region 2 Development')
        plt.title('Development Phase Space')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
        
    def generate_report(self, metrics):
        """Generate analysis report"""
        report = "International Cooperation Analysis\n"
        report += "===============================\n\n"
        
        report += "Model Parameters:\n"
        report += f"Technology Transfer Rate: {self.tech_transfer_rate:.2f}\n"
        report += f"Trade Growth Rate: {self.trade_growth_rate:.2f}\n"
        report += f"Collaboration Factor: {self.collaboration_factor:.2f}\n"
        report += f"Resource Constraint: {self.resource_constraint:.2f}\n\n"
        
        report += "Results:\n"
        for metric, value in metrics.items():
            report += f"{metric}: {value:.2f}\n"
        
        return report

def main():
    # Create model instance
    model = InternationalCooperationModel()
    
    # Run simulation
    t, solution = model.simulate_cooperation()
    
    # Calculate metrics
    metrics = model.calculate_metrics(solution)
    
    # Generate and print report
    print(model.generate_report(metrics))
    
    # Plot results
    model.plot_results(t, solution)

if __name__ == "__main__":
    main()
