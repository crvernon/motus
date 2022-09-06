import pandas as pd
from hamilton import driver

import motus.components as components


class Model:
    """Generate a model.

    :param inputs:                              Dictionary of parameter inputs required to construct the nodes
    :type inputs:                               dict

    :param outputs:                             List of output parameter names to generate.
    :type outputs:                              list




    """

    def __init__(self, inputs: dict, outputs: list):

        # dictionary of parameter inputs required to construct the nodes
        self.inputs = inputs

        # target parameters
        self.outputs = outputs

        # instantiate driver with function definitions
        self.dr = driver.Driver(self.inputs, components)

    def generate(self) -> pd.DataFrame:
        """Run the driver."""

        # generate initial data frame
        df = self.dr.execute(self.outputs)

        return df

    def graph(self):
        """Show the DAG."""

        self.dr.visualize_execution(final_vars=self.outputs,
                                    output_file_path="/Users/d3y010/Desktop/graph.dot",
                                    render_kwargs={'view': True})

    def list_parameters(self):
        """List all available parameters."""

        return self.dr.list_available_variables()


def wrf_to_xanthos():
    """Process WRF outputs for use in Xanthos.

    """

    pass


def wrf_to_tell():
    """Process WRF outputs for use in TELL.

    """

    pass


def wrf_to_helios():
    """Process WRF outputs for use in Helios.

    """

    pass





