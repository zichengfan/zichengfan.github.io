#!/usr/bin/env python3
"""
Script to create animated GIFs for research workflow visualization
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def create_research_workflow_gif():
    """Create an animated GIF showing research workflow"""
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Research workflow steps
    steps = [
        "Data Collection\n(Street View Images)",
        "Preprocessing\n(Image Enhancement)",
        "Deep Learning\n(Feature Extraction)", 
        "Urban Analysis\n(Pattern Recognition)",
        "3D Modeling\n(Environment Simulation)",
        "Results & Insights\n(Urban Planning)"
    ]
    
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe']
    
    def animate(frame):
        ax.clear()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)
        
        # Draw workflow boxes
        for i in range(len(steps)):
            alpha = 1.0 if i <= frame else 0.3
            
            # Box
            rect = plt.Rectangle((i*1.5 + 0.5, 2), 1.2, 2, 
                               facecolor=colors[i], alpha=alpha, 
                               edgecolor='white', linewidth=2)
            ax.add_patch(rect)
            
            # Text
            ax.text(i*1.5 + 1.1, 3, steps[i], 
                   ha='center', va='center', fontsize=8, 
                   color='white', weight='bold', alpha=alpha)
            
            # Arrow
            if i < len(steps) - 1:
                ax.arrow(i*1.5 + 1.7, 3, 0.6, 0, head_width=0.1, 
                        head_length=0.1, fc='gray', alpha=alpha)
        
        ax.set_title('Urban Analytics Research Workflow', 
                    fontsize=16, weight='bold', color='#2c3e50')
        ax.axis('off')
    
    # Create animation
    ani = animation.FuncAnimation(fig, animate, frames=len(steps)+1, 
                                interval=1000, repeat=True, blit=False)
    
    # Save as GIF
    output_path = '../images/research-workflow.gif'
    ani.save(output_path, writer='pillow', fps=1)
    plt.close()
    
    print(f"Research workflow GIF created: {output_path}")

def create_urban_analysis_gif():
    """Create GIF showing urban analysis process"""
    
    # This would use your actual research images
    # For now, creating a conceptual visualization
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))
    
    def animate(frame):
        # Clear all axes
        for ax in [ax1, ax2, ax3, ax4]:
            ax.clear()
        
        # Simulate different analysis stages
        stages = ['Raw Image', 'Feature Detection', 'Semantic Segmentation', '3D Reconstruction']
        
        for i, (ax, stage) in enumerate(zip([ax1, ax2, ax3, ax4], stages)):
            if i <= frame:
                # Create sample visualization for each stage
                data = np.random.rand(50, 50)
                if i == 0:  # Raw image
                    ax.imshow(data, cmap='viridis')
                elif i == 1:  # Feature detection
                    ax.scatter(np.random.rand(20)*50, np.random.rand(20)*50, 
                             c='red', s=50)
                elif i == 2:  # Segmentation
                    ax.imshow(data > 0.5, cmap='Set1')
                else:  # 3D reconstruction
                    from mpl_toolkits.mplot3d import Axes3D
                    ax.remove()
                    ax = fig.add_subplot(2, 2, 4, projection='3d')
                    x, y = np.meshgrid(range(10), range(10))
                    z = np.sin(x/2) * np.cos(y/2)
                    ax.plot_surface(x, y, z, cmap='coolwarm')
            
            ax.set_title(stage, fontsize=12, weight='bold')
            ax.axis('off')
    
    ani = animation.FuncAnimation(fig, animate, frames=4, 
                                interval=1500, repeat=True)
    
    output_path = '../images/urban-analysis.gif'
    ani.save(output_path, writer='pillow', fps=0.67)
    plt.close()
    
    print(f"Urban analysis GIF created: {output_path}")

if __name__ == "__main__":
    # Create the GIFs
    create_research_workflow_gif()
    create_urban_analysis_gif()
    print("All research GIFs created successfully!")