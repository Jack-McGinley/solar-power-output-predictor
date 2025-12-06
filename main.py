#Import Classes from other modules
from Data_Configuration import Data_Config as DC
from PlotAnalysis import PlotAnalysis as PA
import raise_input

file_path = "C:\\Users\\jackp\\Documents\\Python\\EE551\\Project\\nsrdb_2024.csv"

#main function to execute program
def main():
    #Provide user with program information
    print("This program uses data collected from the NSRDB to predict the output power of solar panel modules.")
    print('Please enter parameters for the solar panel model you wish to simulate.')
    while True:
        #User can opt to use default parameters or input their own
        if input('Use default parameters? (y/n): ') == 'y':
            config = DC(file_path) #Use default parameters in Data_Config class 
        else:
            A, E, T, N = raise_input.get_user_input()

            config = DC(file_path, A, E, T, N) #Pass attributes to Data_Config class
        #Return configured CSV file, including power output based on user parameters
        csv_file = config.configure()
        #Create PlotAnalysis object with configured CSV file
        plotter = PA(csv_file)
        #Save figure of plot analysis
        plotter.plot_power_vs_time()
        #Notify user of saved file and configured file
        print(f'Configured data saved to {csv_file}')
        print('Plot saved as solar_power_output.png')
        #Ask user if they would like to try new parameters
        print('Would you like to try new parameters? (y/n): ')
        choice = input()
        if choice.lower() == 'y':
            continue
        elif choice.lower() == 'n':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid input.')
            break

if __name__ == "__main__":
    main()