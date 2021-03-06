import unittest
from script.ccc.conf_spacin import reference_dir, base_iri, context_path, info_dir, triplestore_url, orcid_conf_path, \
    base_dir, temp_dir_for_rdf_loading, context_file_path, dir_split_number, items_per_file, triplestore_url_real, \
    dataset_home, reference_dir_done, reference_dir_error, interface, supplier_dir, default_dir, do_parallel, \
    sharing_dir
import json
from script.spacin.resfinder import ResourceFinder as RF_1
from script.spacin.orcidfinder import ORCIDFinder
from script.spacin.crossrefproc import CrossrefProcessor as CrossrefProcessor
import os
import tracemalloc
tracemalloc.start()

__author__ = 'Gabriele Pisciotta'

class Test(unittest.TestCase):
    maxDiff = None
    def setUp(self):
        self.real_dir = default_dir
        self.supplier_prefix = "070"
        self.full_reference_dir = reference_dir + self.real_dir
        self.full_info_dir = info_dir + self.real_dir

        self.TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        self.orcid_conf_path  = os.path.join(self.TEST_DIR, '..', 'orcid_conf.json')
        with open(os.path.join(self.TEST_DIR, 'test_json.json')) as fp:
            self.json_object = json.load(fp)

    def test_time_processfile(self):

        """with open(os.path.join(self.TEST_DIR, '1.json')) as fp:
            self.json_object = json.load(fp)
            cp = CrossrefProcessor(base_iri, context_path, self.full_info_dir, self.json_object,
                      RF_1(ts_url=triplestore_url, default_dir=default_dir),
                      ORCIDFinder(self.orcid_conf_path, query_interface='remote'), items_per_file,
                      self.supplier_prefix, intext_refs=True, query_interface='remote')
            ret = cp.process()
            with open('1_remote.txt', 'w') as f:
                for g in ret.g:
                    for (s, o, p) in g:
                        f.write(f"{s}, {o}, {p}")"""

        with open(os.path.join(self.TEST_DIR, '1.json')) as fp:
            self.json_object = json.load(fp)
            cp = CrossrefProcessor(base_iri, context_path, self.full_info_dir, self.json_object,
                      RF_1(ts_url=triplestore_url, default_dir=default_dir),
                      ORCIDFinder(self.orcid_conf_path, query_interface='remote'), items_per_file,
                      self.supplier_prefix, intext_refs=True, query_interface='remote')
            ret = cp.process()
            with open('1_remote.txt', 'w') as f:
                for g in ret.g:
                    for (s, o, p) in g:
                        f.write(f"{s}, {o}, {p}")

    def asd(self):
        import time
        """"
        cp = CP_1(base_iri, context_path, self.full_info_dir, self.json_object,
                               RF_1(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='local'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='local')
        s = time.time()
        ret = cp.process()
        e = time.time()
        print(f"Time {(e-s)}")
        print(f"Printing graph")
        n = 0
        with open('graph_1.txt', 'w') as f:
            for g in ret.g:
                for (s, o, p) in g:
                    f.write(f"{s}, {o}, {p}")
                    n+=1
        print(f"NNN SEQ: {n}")

        
        cp = CP_2(base_iri, context_path, self.full_info_dir, self.json_object,
                               RF_2(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='local'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='local')
        s = time.time()
        ret = cp.process()
        e = time.time()
        print(f"Time {(e-s)}")
        print(f"Printing graph")
        n = 0
        ss = set()
        with open('graph_3.txt', 'w') as f:
            for g in ret.g:
                for (s, o, p) in g:
                    ss.add(f"{s}{o}{p}") # in the parallel version we have 1552, in this 1587
                    #f.write(f"{s}, {o}, {p}")
                    n+=1
        print(f"NNN OLD: {len(ss)}") #6176
        print(f"Process existing id time: {cp.process_existing_by_id_time}")
        s = 0
        for index, v in enumerate(cp.lengths):
            print(index, " ", v)
        
        """

        """cp = CP_PAR(base_iri, context_path, self.full_info_dir, self.json_object,
                               RF_1(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='local'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='local')
        s = time.time()
        ret = cp.process()
        e = time.time()
        print(f"Time {(e-s)}")

        n = 0
        ss = set()
        with open('graph_2.txt', 'w') as f:
            for g in ret.g:
                for (s, o, p) in g:
                    #f.write(f"{s}, {o}, {p}")
                    ss.add(f"{s}{o}{p}")
                    n+=1
        print(f"NNN PAR: {len(ss)}") #1552"""

        #s = 0
        #for index, v in enumerate(cp.lengths):
        #    print(index, " ", v)


    """
    def test_wrong_initialization(self):
        self.assertRaises(ValueError, CrossrefProcessor, base_iri, context_path, self.full_info_dir, self.json_object,
                                                    ResourceFinder(ts_url=triplestore_url, default_dir=default_dir),
                                                    ORCIDFinder(self.orcid_conf_path), items_per_file, self.supplier_prefix,
                                                    intext_refs=True, query_interface='asdasd')

    def test_process_doi_remote(self):
        cp = CrossrefProcessor(base_iri, context_path, self.full_info_dir, self.json_object,
                               ResourceFinder(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='remote'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='remote')
        doi = '10.1080/22221751.2020.1766381'
        doi_curator = 'https://api.crossref.org/works/'
        doi_source_provider = 'Informa UK Limited'
        result = cp.process_doi(doi, doi_curator, doi_source_provider, True)
        should_be = {'indexed': {'date-parts': [[2020, 6, 19]], 'date-time': '2020-06-19T20:40:33Z', 'timestamp': 1592599233611}, 'reference-count': 51, 'publisher': 'Informa UK Limited', 'issue': '1', 'license': [{'URL': 'http://creativecommons.org/licenses/by/4.0/', 'start': {'date-parts': [[2020, 1, 1]], 'date-time': '2020-01-01T00:00:00Z', 'timestamp': 1577836800000}, 'delay-in-days': 0, 'content-version': 'unspecified'}], 'content-domain': {'domain': ['www.tandfonline.com'], 'crossmark-restriction': True}, 'short-container-title': ['Emerging Microbes & Infections'], 'published-print': {'date-parts': [[2020, 1, 1]]}, 'DOI': '10.1080/22221751.2020.1766381', 'type': 'journal-article', 'created': {'date-parts': [[2020, 5, 27]], 'date-time': '2020-05-27T16:38:13Z', 'timestamp': 1590597493000}, 'page': '1055-1064', 'update-policy': 'http://dx.doi.org/10.1080/tandf_crossmark_01', 'source': 'Crossref', 'is-referenced-by-count': 0, 'title': ['Households as hotspots of Lassa fever? Assessing the spatial distribution of Lassa virus-infected rodents in rural villages of Guinea'], 'prefix': '10.1080', 'volume': '9', 'author': [{'ORCID': 'http://orcid.org/0000-0001-7023-445X', 'authenticated-orcid': False, 'given': 'Joachim', 'family': 'Mariën', 'sequence': 'first', 'affiliation': [{'name': 'Department of Clinical Sciences/Outbreak Research Team, Institute of Tropical Medicine, Antwerp, Belgium'}]}, {'given': 'Giovanni', 'family': 'Lo Iacono', 'sequence': 'additional', 'affiliation': [{'name': 'School of Veterinary Medicine, University of Surrey, Guildford, UK'}]}, {'given': 'Toni', 'family': 'Rieger', 'sequence': 'additional', 'affiliation': [{'name': 'Bernhard-Nocht-Institute for Tropical Medicine, Hamburg, Germany'}]}, {'given': 'Nfaly', 'family': 'Magassouba', 'sequence': 'additional', 'affiliation': [{'name': 'Laboratoire des Fièvres Hémorragiques, Nongo, Conakry, Guinea'}]}, {'given': 'Stephan', 'family': 'Günther', 'sequence': 'additional', 'affiliation': [{'name': 'Bernhard-Nocht-Institute for Tropical Medicine, Hamburg, Germany'}]}, {'given': 'Elisabeth', 'family': 'Fichet-Calvet', 'sequence': 'additional', 'affiliation': [{'name': 'Bernhard-Nocht-Institute for Tropical Medicine, Hamburg, Germany'}]}], 'member': '301', 'published-online': {'date-parts': [[2020, 5, 27]]}, 'reference': [{'key': 'CIT0001', 'DOI': '10.7717/peerj.533', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0002', 'author': 'Neiderud CJ.', 'volume': '5', 'year': '2015', 'journal-title': 'African J Disabil'}, {'key': 'CIT0003', 'DOI': '10.4269/ajtmh.16-0427', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0004', 'DOI': '10.1016/j.apgeog.2014.02.003', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0005', 'author': 'Olarinmoye AO', 'volume': '12', 'first-page': '8', 'year': '2016', 'journal-title': 'Epizoot Anim Heal West Africa'}, {'key': 'CIT0006', 'DOI': '10.1016/j.tvjl.2017.02.009', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0007', 'DOI': '10.1086/605375', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0008', 'DOI': '10.1371/journal.pntd.0004460', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0009', 'DOI': '10.1890/110111', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0010', 'DOI': '10.1016/j.cosust.2019.05.005', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0011', 'DOI': '10.1089/15303660160025912', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0012', 'DOI': '10.4269/ajtmh.1983.32.829', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0013', 'DOI': '10.1038/srep21977', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0014', 'DOI': '10.1093/infdis/155.3.437', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0015', 'DOI': '10.1080/14772000.2017.1358220', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0016', 'DOI': '10.1186/s13071-018-2991-5', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0017', 'DOI': '10.1089/vbz.2006.0520', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0018', 'author': 'Fichet-calvet E', 'volume': '48', 'first-page': '600', 'year': '2009', 'journal-title': 'Afr J Ecol'}, {'key': 'CIT0019', 'DOI': '10.1002/jmv.1890140402', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0020', 'author': 'McCormick JB.', 'year': '1999', 'volume-title': 'Emergence'}, {'key': 'CIT0021', 'DOI': '10.1007/s10393-016-1098-8', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0022', 'DOI': '10.1371/journal.pntd.0000548', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0023', 'DOI': '10.1371/journal.pntd.0003398', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0024', 'DOI': '10.1089/vbz.2007.0118', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0025', 'DOI': '10.1007/s10393-018-1331-8', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0026', 'DOI': '10.1111/tmi.12259', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0027', 'DOI': '10.1515/MAMM.2008.025', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0028', 'DOI': '10.1111/oik.03623', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0029', 'DOI': '10.1089/vbz.2005.5.305', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0030', 'DOI': '10.1080/22221751.2019.1605846', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0031', 'author': 'Sáez AM', 'volume': '12', 'first-page': '1', 'year': '2018', 'journal-title': 'PLoS Negl Trop Dis'}, {'key': 'CIT0032', 'author': 'Mills JN', 'year': '1995', 'volume-title': 'Methods for trapping and sampling small mammals for virologic testing'}, {'key': 'CIT0033', 'DOI': '10.1016/j.virol.2003.09.009', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0034', 'DOI': '10.1093/molbev/mss075', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0035', 'DOI': '10.1007/BF01313953', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0036', 'DOI': '10.1089/vbz.2013.1484', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0037', 'author': 'Cuzick J', 'volume': '52', 'first-page': '73', 'year': '1990', 'journal-title': 'R Stat Soc'}, {'key': 'CIT0038', 'DOI': '10.1080/03610929708831995', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0039', 'author': 'Borremans B', 'first-page': '1', 'year': '2015', 'journal-title': 'Nat Publ Gr'}, {'key': 'CIT0040', 'author': 'Walker DH', 'volume': '52', 'first-page': '523', 'year': '1975', 'journal-title': 'Bull World Health Organ'}, {'key': 'CIT0041', 'DOI': '10.1007/s10393-017-1256-7', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0042', 'author': 'Leirs H.', 'year': '1994', 'volume-title': 'Population ecology of Mastomys natalensis (Smith, 1834). Implications for rodent control in Africa'}, {'key': 'CIT0044', 'DOI': '10.4269/ajtmh.16-0675', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0045', 'DOI': '10.1007/s10144-013-0393-2', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0046', 'author': 'Mariën J', 'volume': '89', 'first-page': '1365', 'year': '2019', 'journal-title': 'J Anim Ecol'}, {'key': 'CIT0047', 'DOI': '10.1089/vbz.2007.0118', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0048', 'DOI': '10.1071/WR10130', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0049', 'author': 'Leirs H', 'volume': '127', 'first-page': '29', 'year': '1997', 'journal-title': 'Belgian J Zool'}, {'key': 'CIT0050', 'DOI': '10.4269/ajtmh.2007.77.169', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0052', 'author': 'Singleton G', 'year': '2010', 'volume-title': 'Rodent outbreaks: ecology and impacts'}, {'key': 'CIT0053', 'DOI': '10.3201/eid2104.141469', 'doi-asserted-by': 'publisher'}], 'container-title': ['Emerging Microbes & Infections'], 'original-title': [], 'language': 'en', 'link': [{'URL': 'https://www.tandfonline.com/doi/pdf/10.1080/22221751.2020.1766381', 'content-type': 'unspecified', 'content-version': 'vor', 'intended-application': 'similarity-checking'}], 'deposited': {'date-parts': [[2020, 6, 19]], 'date-time': '2020-06-19T19:58:54Z', 'timestamp': 1592596734000}, 'score': 1.0, 'subtitle': [], 'short-title': [], 'issued': {'date-parts': [[2020, 1, 1]]}, 'references-count': 51, 'journal-issue': {'published-print': {'date-parts': [[2020, 1, 1]]}, 'issue': '1'}, 'alternative-id': ['10.1080/22221751.2020.1766381'], 'URL': 'http://dx.doi.org/10.1080/22221751.2020.1766381', 'relation': {'cites': []}, 'ISSN': ['2222-1751'], 'issn-type': [{'value': '2222-1751', 'type': 'electronic'}], 'subject': ['Immunology', 'Epidemiology', 'Microbiology', 'Drug Discovery', 'Parasitology', 'Virology', 'Infectious Diseases', 'General Medicine'], 'assertion': [{'value': 'The publishing and review policy for this title is described in its Aims & Scope.', 'order': 1, 'name': 'peerreview_statement', 'label': 'Peer Review Statement'}, {'value': 'http://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=temi20', 'URL': 'http://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=temi20', 'order': 2, 'name': 'aims_and_scope_url', 'label': 'Aim & Scope'}, {'value': '2020-02-28', 'order': 0, 'name': 'received', 'label': 'Received', 'group': {'name': 'publication_history', 'label': 'Publication History'}}, {'value': '2020-04-24', 'order': 1, 'name': 'revised', 'label': 'Revised', 'group': {'name': 'publication_history', 'label': 'Publication History'}}, {'value': '2020-05-02', 'order': 2, 'name': 'accepted', 'label': 'Accepted', 'group': {'name': 'publication_history', 'label': 'Publication History'}}, {'value': '2020-05-27', 'order': 3, 'name': 'published', 'label': 'Published', 'group': {'name': 'publication_history', 'label': 'Publication History'}}]}
        self.assertEqual(result['DOI'], should_be['DOI'])

    def test_process_doi_local(self):
        cp = CrossrefProcessor(base_iri, context_path, self.full_info_dir, self.json_object,
                               ResourceFinder(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='local'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='local')
        doi = '10.1080/22221751.2020.1766381'
        doi_curator = 'https://api.crossref.org/works/'
        doi_source_provider = 'Informa UK Limited'
        result = cp.process_doi(doi, doi_curator, doi_source_provider, True)
        should_be = {'indexed': {'date-parts': [[2020, 6, 19]], 'date-time': '2020-06-19T20:40:33Z', 'timestamp': 1592599233611}, 'reference-count': 51, 'publisher': 'Informa UK Limited', 'issue': '1', 'license': [{'URL': 'http://creativecommons.org/licenses/by/4.0/', 'start': {'date-parts': [[2020, 1, 1]], 'date-time': '2020-01-01T00:00:00Z', 'timestamp': 1577836800000}, 'delay-in-days': 0, 'content-version': 'unspecified'}], 'content-domain': {'domain': ['www.tandfonline.com'], 'crossmark-restriction': True}, 'short-container-title': ['Emerging Microbes & Infections'], 'published-print': {'date-parts': [[2020, 1, 1]]}, 'DOI': '10.1080/22221751.2020.1766381', 'type': 'journal-article', 'created': {'date-parts': [[2020, 5, 27]], 'date-time': '2020-05-27T16:38:13Z', 'timestamp': 1590597493000}, 'page': '1055-1064', 'update-policy': 'http://dx.doi.org/10.1080/tandf_crossmark_01', 'source': 'Crossref', 'is-referenced-by-count': 0, 'title': ['Households as hotspots of Lassa fever? Assessing the spatial distribution of Lassa virus-infected rodents in rural villages of Guinea'], 'prefix': '10.1080', 'volume': '9', 'author': [{'ORCID': 'http://orcid.org/0000-0001-7023-445X', 'authenticated-orcid': False, 'given': 'Joachim', 'family': 'Mariën', 'sequence': 'first', 'affiliation': [{'name': 'Department of Clinical Sciences/Outbreak Research Team, Institute of Tropical Medicine, Antwerp, Belgium'}]}, {'given': 'Giovanni', 'family': 'Lo Iacono', 'sequence': 'additional', 'affiliation': [{'name': 'School of Veterinary Medicine, University of Surrey, Guildford, UK'}]}, {'given': 'Toni', 'family': 'Rieger', 'sequence': 'additional', 'affiliation': [{'name': 'Bernhard-Nocht-Institute for Tropical Medicine, Hamburg, Germany'}]}, {'given': 'Nfaly', 'family': 'Magassouba', 'sequence': 'additional', 'affiliation': [{'name': 'Laboratoire des Fièvres Hémorragiques, Nongo, Conakry, Guinea'}]}, {'given': 'Stephan', 'family': 'Günther', 'sequence': 'additional', 'affiliation': [{'name': 'Bernhard-Nocht-Institute for Tropical Medicine, Hamburg, Germany'}]}, {'given': 'Elisabeth', 'family': 'Fichet-Calvet', 'sequence': 'additional', 'affiliation': [{'name': 'Bernhard-Nocht-Institute for Tropical Medicine, Hamburg, Germany'}]}], 'member': '301', 'published-online': {'date-parts': [[2020, 5, 27]]}, 'reference': [{'key': 'CIT0001', 'DOI': '10.7717/peerj.533', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0002', 'author': 'Neiderud CJ.', 'volume': '5', 'year': '2015', 'journal-title': 'African J Disabil'}, {'key': 'CIT0003', 'DOI': '10.4269/ajtmh.16-0427', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0004', 'DOI': '10.1016/j.apgeog.2014.02.003', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0005', 'author': 'Olarinmoye AO', 'volume': '12', 'first-page': '8', 'year': '2016', 'journal-title': 'Epizoot Anim Heal West Africa'}, {'key': 'CIT0006', 'DOI': '10.1016/j.tvjl.2017.02.009', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0007', 'DOI': '10.1086/605375', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0008', 'DOI': '10.1371/journal.pntd.0004460', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0009', 'DOI': '10.1890/110111', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0010', 'DOI': '10.1016/j.cosust.2019.05.005', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0011', 'DOI': '10.1089/15303660160025912', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0012', 'DOI': '10.4269/ajtmh.1983.32.829', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0013', 'DOI': '10.1038/srep21977', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0014', 'DOI': '10.1093/infdis/155.3.437', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0015', 'DOI': '10.1080/14772000.2017.1358220', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0016', 'DOI': '10.1186/s13071-018-2991-5', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0017', 'DOI': '10.1089/vbz.2006.0520', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0018', 'author': 'Fichet-calvet E', 'volume': '48', 'first-page': '600', 'year': '2009', 'journal-title': 'Afr J Ecol'}, {'key': 'CIT0019', 'DOI': '10.1002/jmv.1890140402', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0020', 'author': 'McCormick JB.', 'year': '1999', 'volume-title': 'Emergence'}, {'key': 'CIT0021', 'DOI': '10.1007/s10393-016-1098-8', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0022', 'DOI': '10.1371/journal.pntd.0000548', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0023', 'DOI': '10.1371/journal.pntd.0003398', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0024', 'DOI': '10.1089/vbz.2007.0118', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0025', 'DOI': '10.1007/s10393-018-1331-8', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0026', 'DOI': '10.1111/tmi.12259', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0027', 'DOI': '10.1515/MAMM.2008.025', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0028', 'DOI': '10.1111/oik.03623', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0029', 'DOI': '10.1089/vbz.2005.5.305', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0030', 'DOI': '10.1080/22221751.2019.1605846', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0031', 'author': 'Sáez AM', 'volume': '12', 'first-page': '1', 'year': '2018', 'journal-title': 'PLoS Negl Trop Dis'}, {'key': 'CIT0032', 'author': 'Mills JN', 'year': '1995', 'volume-title': 'Methods for trapping and sampling small mammals for virologic testing'}, {'key': 'CIT0033', 'DOI': '10.1016/j.virol.2003.09.009', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0034', 'DOI': '10.1093/molbev/mss075', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0035', 'DOI': '10.1007/BF01313953', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0036', 'DOI': '10.1089/vbz.2013.1484', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0037', 'author': 'Cuzick J', 'volume': '52', 'first-page': '73', 'year': '1990', 'journal-title': 'R Stat Soc'}, {'key': 'CIT0038', 'DOI': '10.1080/03610929708831995', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0039', 'author': 'Borremans B', 'first-page': '1', 'year': '2015', 'journal-title': 'Nat Publ Gr'}, {'key': 'CIT0040', 'author': 'Walker DH', 'volume': '52', 'first-page': '523', 'year': '1975', 'journal-title': 'Bull World Health Organ'}, {'key': 'CIT0041', 'DOI': '10.1007/s10393-017-1256-7', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0042', 'author': 'Leirs H.', 'year': '1994', 'volume-title': 'Population ecology of Mastomys natalensis (Smith, 1834). Implications for rodent control in Africa'}, {'key': 'CIT0044', 'DOI': '10.4269/ajtmh.16-0675', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0045', 'DOI': '10.1007/s10144-013-0393-2', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0046', 'author': 'Mariën J', 'volume': '89', 'first-page': '1365', 'year': '2019', 'journal-title': 'J Anim Ecol'}, {'key': 'CIT0047', 'DOI': '10.1089/vbz.2007.0118', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0048', 'DOI': '10.1071/WR10130', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0049', 'author': 'Leirs H', 'volume': '127', 'first-page': '29', 'year': '1997', 'journal-title': 'Belgian J Zool'}, {'key': 'CIT0050', 'DOI': '10.4269/ajtmh.2007.77.169', 'doi-asserted-by': 'publisher'}, {'key': 'CIT0052', 'author': 'Singleton G', 'year': '2010', 'volume-title': 'Rodent outbreaks: ecology and impacts'}, {'key': 'CIT0053', 'DOI': '10.3201/eid2104.141469', 'doi-asserted-by': 'publisher'}], 'container-title': ['Emerging Microbes & Infections'], 'original-title': [], 'language': 'en', 'link': [{'URL': 'https://www.tandfonline.com/doi/pdf/10.1080/22221751.2020.1766381', 'content-type': 'unspecified', 'content-version': 'vor', 'intended-application': 'similarity-checking'}], 'deposited': {'date-parts': [[2020, 6, 19]], 'date-time': '2020-06-19T19:58:54Z', 'timestamp': 1592596734000}, 'score': 1.0, 'subtitle': [], 'short-title': [], 'issued': {'date-parts': [[2020, 1, 1]]}, 'references-count': 51, 'journal-issue': {'published-print': {'date-parts': [[2020, 1, 1]]}, 'issue': '1'}, 'alternative-id': ['10.1080/22221751.2020.1766381'], 'URL': 'http://dx.doi.org/10.1080/22221751.2020.1766381', 'relation': {'cites': []}, 'ISSN': ['2222-1751'], 'issn-type': [{'value': '2222-1751', 'type': 'electronic'}], 'subject': ['Immunology', 'Epidemiology', 'Microbiology', 'Drug Discovery', 'Parasitology', 'Virology', 'Infectious Diseases', 'General Medicine'], 'assertion': [{'value': 'The publishing and review policy for this title is described in its Aims & Scope.', 'order': 1, 'name': 'peerreview_statement', 'label': 'Peer Review Statement'}, {'value': 'http://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=temi20', 'URL': 'http://www.tandfonline.com/action/journalInformation?show=aimsScope&journalCode=temi20', 'order': 2, 'name': 'aims_and_scope_url', 'label': 'Aim & Scope'}, {'value': '2020-02-28', 'order': 0, 'name': 'received', 'label': 'Received', 'group': {'name': 'publication_history', 'label': 'Publication History'}}, {'value': '2020-04-24', 'order': 1, 'name': 'revised', 'label': 'Revised', 'group': {'name': 'publication_history', 'label': 'Publication History'}}, {'value': '2020-05-02', 'order': 2, 'name': 'accepted', 'label': 'Accepted', 'group': {'name': 'publication_history', 'label': 'Publication History'}}, {'value': '2020-05-27', 'order': 3, 'name': 'published', 'label': 'Published', 'group': {'name': 'publication_history', 'label': 'Publication History'}}]}
        self.assertEqual(result, should_be)

    def test_process_entry_remote(self):
        cp = CrossrefProcessor(base_iri, context_path, self.full_info_dir, self.json_object,
                               ResourceFinder(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='remote'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='remote')
        entry = "Armién, B, Ortiz, PL, Gonzalez, P, et al. Spatial-temporal distribution of Hantavirus rodent-borne infection by Oligoryzomys fulvescens in the Agua Buena region –Panama. PLoS Negl Trop Dis. 2016; 10 DOI: DOI: 10.1371/journal.pntd.0004460."
        should_be = '10.1371/journal.pntd.0004460'
        result = cp.process_entry(entry, True)
        self.assertEqual(result['DOI'], should_be)
        
    def test_process_entry_local(self):
        cp = CrossrefProcessor(base_iri, context_path, self.full_info_dir, self.json_object,
                               ResourceFinder(ts_url=triplestore_url, default_dir=default_dir),
                               ORCIDFinder(self.orcid_conf_path, query_interface='local'), items_per_file,
                               self.supplier_prefix, intext_refs=True, query_interface='local')
        entry = "Armién, B, Ortiz, PL, Gonzalez, P, et al. Spatial-temporal distribution of Hantavirus rodent-borne infection by Oligoryzomys fulvescens in the Agua Buena region –Panama. PLoS Negl Trop Dis. 2016; 10 DOI: DOI: 10.1371/journal.pntd.0004460."
        should_be = '10.1371/journal.pntd.0004460'
        result = cp.process_entry(entry, True)
        self.assertEqual(result['DOI'], should_be)
    """
if __name__ == '__main__':
    unittest.main()
