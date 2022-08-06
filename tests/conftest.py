"""Test configurations and fixtures."""
from typing import Dict, List, Union

import numpy as np
import pkg_resources
import pytest
from gensim.models import KeyedVectors
from wefe.datasets.datasets import fetch_debias_multiclass, fetch_debiaswe, load_weat
from wefe.query import Query
from wefe.utils import load_test_model
from wefe.word_embedding_model import WordEmbeddingModel

# -------------------------------------------------------------------------------------
# Models
# -------------------------------------------------------------------------------------


@pytest.fixture
def keyed_vector_model() -> KeyedVectors:

    resource_package = __name__
    resource_path = "/".join(("datasets", "data", "test_model.kv"))
    weat_w2v_path = pkg_resources.resource_filename(resource_package, resource_path)

    test_model = KeyedVectors.load(weat_w2v_path)
    return test_model


@pytest.fixture
def model() -> WordEmbeddingModel:
    """Load a subset of Word2vec as a testing model.

    Returns
    -------
    WordEmbeddingModel
        The loaded testing model.
    """
    return load_test_model()


# -------------------------------------------------------------------------------------
# Word sets
# -------------------------------------------------------------------------------------


@pytest.fixture
def weat_wordsets() -> Dict[str, List[str]]:
    """Load the word sets used in WEAT original work.

    Returns
    -------
    Dict[str, List[str]]
        A dictionary that map a word set name to a set of words.
    """
    weat_wordsets = load_weat()
    return weat_wordsets


@pytest.fixture
def debiaswe_wordsets() -> Dict[str, List[str]]:
    debiaswe_wordsets = fetch_debiaswe()
    return debiaswe_wordsets


@pytest.fixture
def definitional_pairs(debiaswe_wordsets) -> List[List[str]]:
    return debiaswe_wordsets["definitional_pairs"]


@pytest.fixture
def equalize_pairs(debiaswe_wordsets) -> List[List[str]]:
    return debiaswe_wordsets["equalize_pairs"]


@pytest.fixture
def gender_specific(debiaswe_wordsets) -> List[str]:
    return debiaswe_wordsets["gender_specific"]


@pytest.fixture
def multiclass_debias_wordsets() -> Dict[str, List[str]]:
    multiclass_debias_wordsets = fetch_debias_multiclass()
    return multiclass_debias_wordsets


@pytest.fixture
def mhd_gender_definitional_sets(multiclass_debias_wordsets) -> List[List[str]]:
    return multiclass_debias_wordsets["gender_definitional_sets"]


@pytest.fixture
def mhd_gender_equalize_sets(multiclass_debias_wordsets) -> List[List[str]]:
    return list(multiclass_debias_wordsets["gender_analogy_templates"].values())


@pytest.fixture
def mhd_ethnicity_definitional_sets(multiclass_debias_wordsets) -> List[List[str]]:
    return multiclass_debias_wordsets["ethnicity_definitional_sets"]


@pytest.fixture
def mhd_ethnicity_equalize_sets(multiclass_debias_wordsets) -> List[List[str]]:
    return list(multiclass_debias_wordsets["ethnicity_analogy_templates"].values())


# -------------------------------------------------------------------------------------
# Queries
# -------------------------------------------------------------------------------------


@pytest.fixture
def query_2t1a_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    weat_wordsets = load_weat()

    query = Query(
        [weat_wordsets["flowers"], weat_wordsets["insects"]],
        [weat_wordsets["pleasant_5"]],
        ["Flowers", "Insects"],
        ["Pleasant"],
    )
    return query


@pytest.fixture
def query_2t2a_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    """Generate a Flower and Insects wrt Pleasant vs Unpleasant test query.

    Parameters
    ----------
    weat_wordsets : Dict[str, List[str]]
        The word sets used in WEAT original work.

    Returns
    -------
    Query
        The generated query.
    """
    query = Query(
        [weat_wordsets["flowers"], weat_wordsets["insects"]],
        [weat_wordsets["pleasant_5"], weat_wordsets["unpleasant_5"]],
        ["Flowers", "Insects"],
        ["Pleasant", "Unpleasant"],
    )
    return query


@pytest.fixture
def query_2t2a_uppercase(weat_wordsets: Dict[str, List[str]]) -> Query:
    """Generate a Flower and Insects wrt Pleasant vs Unpleasant test query.

    Parameters
    ----------
    weat_wordsets : Dict[str, List[str]]
        The word sets used in WEAT original work.

    Returns
    -------
    Query
        The generated query.
    """
    query = Query(
        [
            [s.upper() for s in weat_wordsets["flowers"]],
            [s.upper() for s in weat_wordsets["insects"]],
        ],
        [
            [s.upper() for s in weat_wordsets["pleasant_5"]],
            [s.upper() for s in weat_wordsets["unpleasant_5"]],
        ],
        ["Flowers", "Insects"],
        ["Pleasant", "Unpleasant"],
    )
    return query


@pytest.fixture
def query_3t2a_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    query = Query(
        [
            weat_wordsets["flowers"],
            weat_wordsets["insects"],
            weat_wordsets["instruments"],
        ],
        [weat_wordsets["pleasant_5"], weat_wordsets["unpleasant_5"]],
        ["Flowers", "Weapons", "Instruments"],
        ["Pleasant", "Unpleasant"],
    )

    return query


@pytest.fixture
def query_4t2a_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    query = Query(
        [
            weat_wordsets["flowers"],
            weat_wordsets["insects"],
            weat_wordsets["instruments"],
            weat_wordsets["weapons"],
        ],
        [weat_wordsets["pleasant_5"], weat_wordsets["unpleasant_5"]],
        ["Flowers", "Insects", "Instruments", "Weapons"],
        ["Pleasant", "Unpleasant"],
    )

    return query


@pytest.fixture
def query_1t4_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    query = Query(
        [weat_wordsets["flowers"]],
        [
            weat_wordsets["pleasant_5"],
            weat_wordsets["pleasant_9"],
            weat_wordsets["unpleasant_5"],
            weat_wordsets["unpleasant_9"],
        ],
        ["Flowers"],
        ["Pleasant 5 ", "Pleasant 9", "Unpleasant 5", "Unpleasant 9"],
    )
    return query


@pytest.fixture
def query_2t1a_lost_vocab_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    query = Query(
        [["bla", "asd"], weat_wordsets["insects"]],
        [weat_wordsets["pleasant_5"]],
        ["Flowers", "Insects"],
        ["Pleasant"],
    )

    return query


@pytest.fixture
def query_2t2a_lost_vocab_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    query = Query(
        [["bla", "asd"], weat_wordsets["insects"]],
        [weat_wordsets["pleasant_5"], weat_wordsets["unpleasant_5"]],
        ["Flowers", "Insects"],
        ["Pleasant", "Unpleasant"],
    )

    return query


# --------------------------------------------------------------------------------------
# 2 target 2 attribute  gender, ethnicity and religion queries
# --------------------------------------------------------------------------------------


@pytest.fixture
def gender_query_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    """Generate a Male and Female names wrt Pleasant vs Unpleasant test query.

    Parameters
    ----------
    weat_wordsets : Dict[str, List[str]]
        The word sets used in WEAT original work.

    Returns
    -------
    Query
        The generated query.
    """
    query = Query(
        [weat_wordsets["male_names"], weat_wordsets["female_names"]],
        [weat_wordsets["pleasant_5"], weat_wordsets["unpleasant_5"]],
        ["Male Names", "Female Names"],
        ["Pleasant", "Unpleasant"],
    )
    return query


@pytest.fixture
def gender_query_2(weat_wordsets: Dict[str, List[str]]) -> Query:
    """Generate a Male and Female names wrt Career vs Family terms test query.

    Parameters
    ----------
    weat_wordsets : Dict[str, List[str]]
        The word sets used in WEAT original work.

    Returns
    -------
    Query
        The generated query.
    """
    query = Query(
        [weat_wordsets["male_names"], weat_wordsets["female_names"]],
        [weat_wordsets["career"], weat_wordsets["family"]],
        ["Male Names", "Female Names"],
        ["Career", "Family"],
    )
    return query


@pytest.fixture
def gender_query_3(
    multiclass_debias_wordsets: Dict[str, Dict[str, Union[List[str], list]]]
) -> Query:
    """Generate a Male and Female names wrt Career vs Family terms test query.

    Parameters
    ----------
    weat_wordsets : Dict[str, List[str]]
        The word sets used in WEAT original work.

    Returns
    -------
    Query
        The generated query.
    """
    gender_eval = (
        np.array(multiclass_debias_wordsets["gender_eval_target"])
        .reshape(2, -1)
        .tolist()
    )
    gender_analogy_templates = np.array(
        list(multiclass_debias_wordsets["gender_analogy_templates"].values())
    ).tolist()
    query = Query(
        [gender_eval[0], gender_eval[1]],
        [gender_analogy_templates[0], gender_analogy_templates[1]],
        target_sets_names=["Male terms", "Female terms"],
        attribute_sets_names=["Male roles", "Female roles"],
    )

    return query


@pytest.fixture
def ethnicity_query_1(weat_wordsets: Dict[str, List[str]]) -> Query:
    """Generate a European and African american names wrt Pleasant vs Unpleasant query.

    Parameters
    ----------
    weat_wordsets : Dict[str, List[str]]
        The word sets used in WEAT original work.

    Returns
    -------
    Query
        The generated query.
    """
    query = Query(
        [
            weat_wordsets["european_american_names_5"],
            weat_wordsets["african_american_names_5"],
        ],
        [weat_wordsets["pleasant_5"], weat_wordsets["unpleasant_5"]],
        ["european_american_names_5", "african_american_names_5"],
        ["pleasant_5", "unpleasant_5"],
    )
    return query
