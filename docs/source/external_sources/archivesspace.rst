=============
ArchivesSpace
=============

Unique Fields from ArchivesSpace
================================

Here are the results of a Schema Analysis from variety.js that lists the unique fields available in oai_dcterms.

+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| key                                               | types                             | occurrences | percents            |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| _id                                               | ObjectId                          | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata                                          | Object                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms                      | Object                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.@xmlns:dcterms       | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.@xmlns:oai_dcterms   | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.@xmlns:xsi           | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.@xsi:schemaLocation  | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:alternative  | String (4414),null (61)           | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:date         | String (4424),Array (51)          | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:extent       | String (4463),Array (12)          | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:identifier   | Array (4444),String (31)          | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:language     | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:publisher    | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:title        | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| oai_provider                                      | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| record_id                                         | String                            | 4475        | 100.000000000000000 |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:accessRights | String (4426),null (22),Array (1) | 4449        | 99.418994413407816  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:description  | Array (4075),String (366)         | 4441        | 99.240223463687144  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:abstract     | String                            | 4418        | 98.726256983240219  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:rights       | String (4389),null (22),Array (3) | 4414        | 98.636871508379883  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:provenance   | String (3272),Array (1)           | 3273        | 73.139664804469277  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:subject      | Array (1556),String (1356)        | 2912        | 65.072625698324018  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:coverage     | String (1095),Array (884)         | 1979        | 44.223463687150840  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:type         | Array (123),String (464)          | 587         | 13.117318435754189  |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+
| metadata.oai_dcterms:dcterms.dcterms:relation     | String (184),Array (163)          | 347         | 7.754189944134078   |
+---------------------------------------------------+-----------------------------------+-------------+---------------------+

Metadata Mapping
================

This metadata mapping maps ArchivesSpace dcterms to Primo VE DublinCore Expanded based on the
`Mapping to the Display, Facets, and Search Sections in the Primo VE Record <https://knowledge.exlibrisgroup.com/Primo/Product_Documentation/020Primo_VE/050Other_Configuration/Mapping_to_the_Display%2C_Facets%2C_and_Search_Sections_in_the_Primo_VE_Record#Dublin_Core_2>`_
and the `Configuring Import Profiles for Primo VE <https://knowledge.exlibrisgroup.com/Primo/Product_Documentation/020Primo_VE/045Loading_Records_from_External_Sources_into_Primo_VE/Configuring_Import_Profiles_for_Primo_VE>`_ documentation.

Metadata in ArchivesSpace is mapped via `oai_dcterms <http://albatross.lib.utk.edu/oai?verb=ListRecords&set=collection&metadataPrefix=oai_dcterms>`_
rather than oai_mods because of an `issue with well-formedness in oai_mods in ArchivesSpace <https://github.com/archivesspace/archivesspace/issues/1687>`_.

+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms              | Primo VE Expanded DublinCore | Display Field                   | Facets Field  | Search Field      |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:title        | dc:title                     | Title                           |               | Title             |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:identifier   | dc:identifier                |                                 |               | General           |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:publisher    | dcterms:publisher            | Publisher                       |               | General           |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:date         | dc:date                      | Creation Date (priority 1)      | Creation Date | Creation Date     |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:extent       | dcterms:extent               | Physical Description and Format |               | Format            |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:language     | dcterms:language             | Language                        | Language      | Language          |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:description  | dcterms:description          | Description                     |               | Description       |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:accessRights | dcterms:accessRights         | Rights                          |               |                   |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:alternative  | dcterms:alternative          | Alternative Title               |               | Alternative Title |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:abstract     | dcterms:abstract             | Description                     |               | Description       |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:rights       | dc:rights                    | Rights                          |               |                   |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:provenance   | dc:terms:description         | Description                     |               | Description       |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:subject      | dc:subject                   | Subjects                        | Topic         | Subjects          |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:coverage     | dcterms:coverage             |                                 |               | General           |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:type         | dc:subject                   | Subjects                        | Topice        | Subjects          |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+
| dcterms:relation     | dcterms:description          | Description                     |               | Description       |
+----------------------+------------------------------+---------------------------------+---------------+-------------------+


Discovery Import Profile
========================

This is the settings for our discovery import profile for ArchivesSpace:


* Base URL: `http://albatross.lib.utk.edu/oai <http://albatross.lib.utk.edu/oai>`_
* Set: collection
* Metadata Prefix: oai_dcterms


Normalization Rules
===================

Below are the original normalization rules when we were trying to use oai_mods and our current normalizaiton rules.

-------------
Current Rules
-------------

.. code-block:: rst
    :name: Copy First Title
    :caption: Copy First Title

    rule "copy first title"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='title'][1]"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='title'][1]" to "dc"."title"
    end


.. code-block:: rst
    :name: Copy All Identifiers
    :caption: Copy All Identifiers

    rule "copy all identifiers"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='identifier']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='identifier']" to "dc"."identifier"
    end

.. code-block:: rst
    :name: Copy publisher
    :caption: Copy publisher

    rule "copy publisher"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='publisher']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='publisher']" to "dcterms"."publisher"
    end

.. code-block:: rst
    :name: Date rules
    :caption: Prioritize first date but copy all dates to a second field

    rule "copy first date to dc:date"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='date'][1]"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='date'][1]" to "dc"."date"
    end

    rule "copy all dates to dcterms:date"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='date']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='date']" to "dcterms"."date"
    end

.. code-block:: rst
    :name: Set Resource Type
    :caption: Set all objects to be an archival material resource type

    rule "set resource type of Archival Materials"
        when
            true
        then
            set "archival_materials" in "discovery"."resourceType"
    end

.. code-block:: rst
    :name: Copy Extent Information
    :caption: Copy Extent Information

    rule "copy all extent infomation to dcterms:extent"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='extent']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='extent']" to "dcterms"."extent"
    end

.. code-block:: rst
    :name: Copy Language Information
    :caption: Copy Language Information

    rule "copy all languages to dcterms:language"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='language']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='language']" to "dcterms"."language"
    end

.. code-block:: rst
    :name: Copy all Descriptions
    :caption: Copy all Descriptions

    rule "copy all descriptions to dcterms:description"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='description']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='description']" to "dcterms"."description"
    end

.. code-block:: rst
    :name: Copy the abstract
    :caption: Copy the abstract

    rule "copy the abstract to dcterms:abstract"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='abstract']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='abstract']" to "dcterms"."abstract"
    end

.. code-block:: rst
    :name: Copy the Access Rights
    :caption: Copy the Access Rights

    rule "copy access rights to dcterms:accessRights"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='accessRights']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='accessRights']" to "dcterms"."accessRights"
    end

.. code-block:: rst
    :name: Copy Alternative Title
    :caption: Copy Alternative Title

    rule "copy alternative titles to dcterms:alternative"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='alternative']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='alternative']" to "dcterms"."alternative"
    end

.. code-block:: rst
    :name: Copy Abstracts
    :caption: Copy Abstracts

    rule "copy abstracts to dcterms:abstract"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='abstract']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='abstract']" to "dcterms"."abstract"
    end

.. code-block:: rst
    :name: Copy Rights
    :caption: Copy Rights

    rule "copy rights to dc:rights"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='rights']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='rights']" to "dc"."rights"
    end

.. code-block:: rst
    :name: Copy Provenance Information to Description
    :caption: Copy Provenance Information to Description

    rule "copy provenance to dcterms:description"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='provenance']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='provenance']" to "dcterms"."description"
    end

.. code-block:: rst
    :name: Copy subjects
    :caption: Copy subjects

    rule "copy subjects to dc:subject"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='subject']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='subject']" to "dc"."subject"
    end

.. code-block:: rst
    :name: Copy Coverage
    :caption: Copy coverage

    rule "copy coverage to dcterms:coverage"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='coverage']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='coverage']" to "dcterms"."coverage"
    end

.. code-block:: rst
    :name: Copy types to dc subject since they aren't really types in ArchivesSpace
    :caption: Copy types to dc subject since they aren't really types in ArchivesSpace

    rule "copy types to subjects"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='type']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='type']" to "dc"."subject"
    end

.. code-block:: rst
    :name: Copy relation to description
    :caption: Copy relation to description

    rule "copy relations to description"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='relation']"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.openarchives.org/OAI/2.0/oai_dcterms/' and local-name()='dcterms'][1]/*[namespace-uri()='http://purl.org/dc/terms/' and local-name()='relation']" to "dcterms"."description"
    end

-------------------------------
Sample Rules (No longer in use)
-------------------------------

.. code-block:: rst
    :name: Original Test MODS Normalization Rules
    :caption: Original Test Rules for MODS

    rule "copy first title"
        when
            exist "/record/metadata[1]/*[namespace-uri()='http://www.loc.gov/mods/v3' and local-name()='mods'][1]/*[namespace-uri()='http://www.loc.gov/mods/v3' and local-name()='titleinfo=='][1]"
        then
            copy "/record/metadata[1]/*[namespace-uri()='http://www.loc.gov/mods/v3' and local-name()='mods'][1]/*[namespace-uri()='http://www.loc.gov/mods/v3' and local-name()='titleinfo'][1]/*[namespace-uri()='http://www.loc.gov/mods/v3' and local-name()='title']" to "dc"."title"
    end

    rule "set resource type of Archival Materials"
        when
            true
        then
            set "archival_materials" in "discovery"."resourceType"
    end

