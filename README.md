# protein-to-gene-conversion-python-script
Python scripts used to switch from protein to gene names in constructed PPINs 

This script is designed to map and replace node identifiers in a tab-delimited network file using a provided mapping file. It is useful when working with biological networks (e.g., protein–protein interaction networks) where identifiers need to be converted (such as protein IDs → gene IDs).

The script:

Reads a mapping file containing pairs of identifiers.

Reads a network file (TSV format) with edges (connections between nodes).

Replaces the first two columns of the network file with their mapped values, if available.

Outputs the modified network to the console (standard output).

**Input files needed**

Mapping file:
   - Must be tab delimitted
   - First column must be original identifier
   - Second column must be the replacement identifier

Network file:
  - Must be tab delimitted
  - First row should be a headers (ignored in mapping, but printed unchanged)
  - First two columns should be node identifiers

**IMPORTANT!!!**

**- Only the first two columns of the network file are mapped**

**- Unmapped codes remain unchanged**

**- The script currently prints to console; redirect output if you want a saved file**
