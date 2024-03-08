"""Example of how to use dynsight.onion."""

import sys
from pathlib import Path

import dynsight


def main() -> None:
    """Run the example.

    If you want to run the code with the example dataset, clone the github
    repo at https://github.com/matteobecchi/onion_example_files and then
    run this script giving as argument

    path/to/folder/onion_example_files/data/multivariate_time-series_0.npy
    path/to/folder/onion_example_files/data/multivariate_time-series_1.npy

    If you are instead using your own data, run this script giving as argument
    the paths to your data.
    """
    first_line = "Usage: python3 onion_uni.py path/to/input/file"
    if len(sys.argv) < 2:  # noqa: PLR2004
        error_log = Path("error_log.txt")
        with error_log.open(mode="w") as file:
            print(f"{first_line}", file=file)
        sys.exit()
    else:
        input_data = sys.argv[1]

    ### Clustering of univariate time-series ###
    onion_2 = dynsight.onion.OnionMulti(
        path_to_input=input_data,
        output_path=Path("./onion_output"),
        tau_w=10,
        t_conv=200,
        t_units="ms",
        example_id=0,
        max_t_smooth=2,
    )

    onion_2.run()

    ### Number of states and fraction of ENV0 for the different
    ### values of tau_window and t_smooth
    ### Each row is a different tau_window, first element is tau_window
    ### then each column is a different t_smooth.
    _ = onion_2.get_number_of_states()
    _ = onion_2.get_fraction_0()

    ### Returns a StateMulti object, with three attributes:
    ### mean [np.adarray], standard deviation [np.adarray],
    ### and percentage of data points [float].
    _ = onion_2.get_state_list()

    ### An array of shape (N, T) with the labels for
    ### all the data points
    _ = onion_2.get_clustering()


if __name__ == "__main__":
    main()
